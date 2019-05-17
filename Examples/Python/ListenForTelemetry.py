import socket
import flatbuffers
import kartkraft.Frame
import kartkraft.Motion

UDP_IP = "10.0.0.1"
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
        print("\nreceived telemetry frame of size ", len(bytes), " from ", addr)
        time = frame.Timestamp()
        motion = frame.Motion()
        dash = frame.Dash()
        session = frame.Session()
        vehicleConfig = frame.VehicleConfig()

        print("time ", time)

        if (motion):
            print("    motion data ", motion.Pitch(), motion.Roll(), motion.Yaw(),
                  motion.AccelerationX(), motion.AccelerationY(), motion.AccelerationZ(),
                  motion.TractionLoss(),
                  motion.VelocityX(), motion.VelocityY(), motion.VelocityZ(),
                  motion.AngularVelocityX(), motion.AngularVelocityY(), motion.AngularVelocityZ())

        if (dash):
            print("    dash data ", dash.Rpm(), dash.Speed(), dash.Steer(), dash.Throttle(), dash.Brake(
            ), dash.Gear(), dash.Pos(), dash.BestLap(), dash.CurrentLap(), dash.LastLap(), dash.Lap())

        if (session):
            print("    session data ",
                  session.TotalTime(), session.TotalTime())

        if (vehicleConfig):
            print("    vehicleConfig data ",
                  vehicleConfig.RpmLimit(), vehicleConfig.RpmMax(), vehicleConfig.GearMax())
