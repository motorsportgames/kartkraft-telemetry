import socket
import flatbuffers
import kartkraft.Frame
import kartkraft.Motion

UDP_IP = "127.0.0.1"
UDP_PORT = 5000
MAX_PACKET_SIZE = 1024

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

print("listening on:", UDP_IP, ":", UDP_PORT)

while True:
    data, addr = sock.recvfrom(MAX_PACKET_SIZE)
    bytes = bytearray(data)
    frame = kartkraft.Frame.Frame.GetRootAsFrame(bytes, 0)
    if (frame):
        print("received telemetry frame of size ", len(bytes))
        motion = frame.Motion()
        dash = frame.Dash()
        session = frame.Session()
        if (motion):
            print("    motion data ", motion.Pitch(), motion.Roll(), motion.Yaw(
            ), motion.AccelerationX(), motion.AccelerationY(), motion.AccelerationZ(), motion.Traction())
        if (dash):
            print("    dash data ", dash.Rpm(), dash.Speed())
        if (session):
            print("    session data ",
                  session.TotalTime(), session.TotalTime())
