import socket
import flatbuffers
import KartKraft.Dashboard
import KartKraft.Frame
import KartKraft.Motion
import KartKraft.Surface
import KartKraft.TrackConfig
import KartKraft.VehicleConfig
import KartKraft.Wheel

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
    KartKraft.Wheel.WheelStart(b)
    KartKraft.Wheel.WheelAddSurface(b, KartKraft.Surface.Surface.Asphalt)
    KartKraft.Wheel.WheelAddSlipAngle(b, x * 0.01)
    wheelOffsets.append(KartKraft.Wheel.WheelEnd(b))

# Add wheels to vector
KartKraft.Motion.MotionStartWheelsVector(b, numWheels)
for offset in wheelOffsets:
    b.PrependUOffsetTRelative(offset)
wheels = b.EndVector(numWheels)

# Create some test motion data
KartKraft.Motion.MotionStart(b)
KartKraft.Motion.MotionAddPitch(b, 0.25)
KartKraft.Motion.MotionAddRoll(b, 0.05)
KartKraft.Motion.MotionAddYaw(b, 43.30)
KartKraft.Motion.MotionAddAngularVelocityX(b, 0.1)
KartKraft.Motion.MotionAddAngularVelocityY(b, -1.2)
KartKraft.Motion.MotionAddAngularVelocityZ(b, 9.3)
KartKraft.Motion.MotionAddVelocityX(b, 22.1)
KartKraft.Motion.MotionAddVelocityY(b, 1.2)
KartKraft.Motion.MotionAddVelocityY(b, 0.3)
KartKraft.Motion.MotionAddAccelerationX(b, 3.1)
KartKraft.Motion.MotionAddAccelerationX(b, -0.2)
KartKraft.Motion.MotionAddAccelerationX(b, 5.3)
KartKraft.Motion.MotionAddTractionLoss(b, -4.3)
KartKraft.Motion.MotionAddWheels(b, wheels)
KartKraft.Motion.MotionAddWorldVelocityX(b, 10.0)
KartKraft.Motion.MotionAddWorldVelocityY(b, 0.1)
KartKraft.Motion.MotionAddWorldVelocityZ(b, 0.2)
motion = KartKraft.Motion.MotionEnd(b)

# Create some test dashboard data
KartKraft.Dashboard.DashboardStart(b)
KartKraft.Dashboard.DashboardAddRpm(b, 1000)
KartKraft.Dashboard.DashboardAddSpeed(b, 12.0)
KartKraft.Dashboard.DashboardAddGear(b, 1)
KartKraft.Dashboard.DashboardAddThrottle(b, 0.75)
KartKraft.Dashboard.DashboardAddBrake(b, 0.25)
KartKraft.Dashboard.DashboardAddBestLap(b, 45.234)
KartKraft.Dashboard.DashboardAddLastLap(b, 47.012)
KartKraft.Dashboard.DashboardAddCurrentLap(b, 13.922)
KartKraft.Dashboard.DashboardAddLapCount(b, 5)
KartKraft.Dashboard.DashboardAddSteer(b, 2.3)
KartKraft.Dashboard.DashboardAddPos(b, 3)
KartKraft.Dashboard.DashboardAddSectorCount(b, 1)
dashboard = KartKraft.Dashboard.DashboardEnd(b)

# Create some test vehicle config data
KartKraft.VehicleConfig.VehicleConfigStart(b)
KartKraft.VehicleConfig.VehicleConfigAddGearMax(b, 1)
KartKraft.VehicleConfig.VehicleConfigAddRpmLimit(b, 15500)
KartKraft.VehicleConfig.VehicleConfigAddRpmMax(b, 16000)
vehicleConfig = KartKraft.VehicleConfig.VehicleConfigEnd(b)

# Create some test track config data
trackName = b.CreateString('Nordschleife')
KartKraft.TrackConfig.TrackConfigStart(b)
KartKraft.TrackConfig.TrackConfigAddName(b, trackName)
KartKraft.TrackConfig.TrackConfigAddNumSectors(b, 3)
trackConfig = KartKraft.TrackConfig.TrackConfigEnd(b)


# Create frame and add the test motion and test dashboard data
KartKraft.Frame.FrameStart(b)
KartKraft.Frame.FrameAddMotion(b, motion)
KartKraft.Frame.FrameAddDash(b, dashboard)
KartKraft.Frame.FrameAddVehicleConfig(b, vehicleConfig)
KartKraft.Frame.FrameAddTrackConfig(b, trackConfig)
frame = KartKraft.Frame.FrameEnd(b)

# Finish writing the flatbuffer and get thte data as raw bytes
b.Finish(frame, str.encode("KKFB")) #add identifier
bytes = b.Output()

print("Sending ", len(bytes), " bytes")

# Send bytes over UDP
sock.sendto(bytes, (UDP_IP, UDP_PORT))
