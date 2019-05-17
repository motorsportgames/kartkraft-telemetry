import socket
import flatbuffers
import kartkraft.Frame
import kartkraft.Motion
import kartkraft.Dashboard

UDP_IP = '10.0.0.6'
UDP_PORT = 5000
MAX_PACKET_SIZE = 1024

print("Sending telemetry to:", UDP_IP, ":", UDP_PORT)

# Create socket
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

# Create flatbuffer builder object
b = flatbuffers.Builder(MAX_PACKET_SIZE)

# Create some test motion data
kartkraft.Motion.MotionStart(b)
kartkraft.Motion.MotionAddPitch(b, 0.25)
motion = kartkraft.Motion.MotionEnd(b)

# Create some test dashboard data
kartkraft.Dashboard.DashboardStart(b)
kartkraft.Dashboard.DashboardAddRpm(b, 1000)
kartkraft.Dashboard.DashboardAddSpeed(b, 12.0)
dashboard = kartkraft.Dashboard.DashboardEnd(b)

# Create frame and add the test motion and test dashboard data
kartkraft.Frame.FrameStart(b)
kartkraft.Frame.FrameAddMotion(b, motion)
kartkraft.Frame.FrameAddDash(b, dashboard)
frame = kartkraft.Frame.FrameEnd(b)

# Finish writing the flatbuffer and get thte data as raw bytes
b.Finish(frame)
bytes = b.Output()

# Send bytes over UDP
sock.sendto(bytes, (UDP_IP, UDP_PORT))
