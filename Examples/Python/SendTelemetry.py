import socket
import flatbuffers
import kartkraft.Dashboard
import kartkraft.Frame
import kartkraft.Motion
import kartkraft.Surface
import kartkraft.TrackConfig
import kartkraft.VehicleConfig
import kartkraft.Wheel

UDP_IP = '127.0.0.1'
UDP_PORT = 5000
MAX_PACKET_SIZE = 1024

print("Sending telemetry to:", UDP_IP, ":", UDP_PORT)

# Create socket
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

# Create flatbuffer builder object
b = flatbuffers.Builder(MAX_PACKET_SIZE)

# Create four wheels
numWheels = 4
wheelOffsets = []
for x in range(numWheels):
    kartkraft.Wheel.WheelStart(b)
    kartkraft.Wheel.WheelAddSurface(b, kartkraft.Surface.Surface.Asphalt)
    kartkraft.Wheel.WheelAddSlipAngle(b, x * 0.01)
    wheelOffsets.append(kartkraft.Wheel.WheelEnd(b))

# Add wheels to vector
kartkraft.Motion.MotionStartWheelsVector(b, numWheels)
for offset in wheelOffsets:
    b.PrependUOffsetTRelative(offset)
wheels = b.EndVector(numWheels)

# Create some test motion data
kartkraft.Motion.MotionStart(b)
kartkraft.Motion.MotionAddPitch(b, 0.25)
kartkraft.Motion.MotionAddRoll(b, 0.05)
kartkraft.Motion.MotionAddYaw(b, 43.30)
kartkraft.Motion.MotionAddAngularVelocityX(b, 0.1)
kartkraft.Motion.MotionAddAngularVelocityY(b, -1.2)
kartkraft.Motion.MotionAddAngularVelocityZ(b, 9.3)
kartkraft.Motion.MotionAddVelocityX(b, 22.1)
kartkraft.Motion.MotionAddVelocityY(b, 1.2)
kartkraft.Motion.MotionAddVelocityY(b, 0.3)
kartkraft.Motion.MotionAddAccelerationX(b, 3.1)
kartkraft.Motion.MotionAddAccelerationX(b, -0.2)
kartkraft.Motion.MotionAddAccelerationX(b, 5.3)
kartkraft.Motion.MotionAddTractionLoss(b, -4.3)
kartkraft.Motion.MotionAddWheels(b, wheels)
kartkraft.Motion.MotionAddWorldVelocityX(b, 10.0)
kartkraft.Motion.MotionAddWorldVelocityY(b, 0.1)
kartkraft.Motion.MotionAddWorldVelocityZ(b, 0.2)
motion = kartkraft.Motion.MotionEnd(b)

# Create some test dashboard data
kartkraft.Dashboard.DashboardStart(b)
kartkraft.Dashboard.DashboardAddRpm(b, 1000)
kartkraft.Dashboard.DashboardAddSpeed(b, 12.0)
kartkraft.Dashboard.DashboardAddGear(b, 1)
kartkraft.Dashboard.DashboardAddThrottle(b, 0.75)
kartkraft.Dashboard.DashboardAddBrake(b, 0.25)
kartkraft.Dashboard.DashboardAddBestLap(b, 45.234)
kartkraft.Dashboard.DashboardAddLastLap(b, 47.012)
kartkraft.Dashboard.DashboardAddCurrentLap(b, 13.922)
kartkraft.Dashboard.DashboardAddLapCount(b, 5)
kartkraft.Dashboard.DashboardAddSteer(b, 2.3)
kartkraft.Dashboard.DashboardAddPos(b, 3)
kartkraft.Dashboard.DashboardAddSectorCount(b, 1)
dashboard = kartkraft.Dashboard.DashboardEnd(b)

# Create some test vehicle config data
kartkraft.VehicleConfig.VehicleConfigStart(b)
kartkraft.VehicleConfig.VehicleConfigAddGearMax(b, 1)
kartkraft.VehicleConfig.VehicleConfigAddRpmLimit(b, 15500)
kartkraft.VehicleConfig.VehicleConfigAddRpmMax(b, 16000)
vehicleConfig = kartkraft.VehicleConfig.VehicleConfigEnd(b)

# Create some test track config data
trackName = b.CreateString('Nordschleife')
kartkraft.TrackConfig.TrackConfigStart(b)
kartkraft.TrackConfig.TrackConfigAddName(b, trackName)
kartkraft.TrackConfig.TrackConfigAddNumSectors(b, 3)
trackConfig = kartkraft.TrackConfig.TrackConfigEnd(b)


# Create frame and add the test motion and test dashboard data
kartkraft.Frame.FrameStart(b)
kartkraft.Frame.FrameAddMotion(b, motion)
kartkraft.Frame.FrameAddDash(b, dashboard)
kartkraft.Frame.FrameAddVehicleConfig(b, vehicleConfig)
kartkraft.Frame.FrameAddTrackConfig(b, trackConfig)
frame = kartkraft.Frame.FrameEnd(b)

# Finish writing the flatbuffer and get thte data as raw bytes
b.Finish(frame)
bytes = b.Output()

# Send bytes over UDP
sock.sendto(bytes, (UDP_IP, UDP_PORT))
