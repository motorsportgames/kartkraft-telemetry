import socket
import flatbuffers
import KartKraft.Frame
import KartKraft.Motion
import KartKraft.Surface
import KartKraft.VehicleConfig
import KartKraft.TrackConfig

UDP_IP = "127.0.0.1"
UDP_PORT = 5000
MAX_PACKET_SIZE = 1024
# flatbuffers python not generating enum names yet, so let's hardcode some values for now
SURFACE_NAMES = ["None", "Asphalt", "Grass", "Gravel", "Kerb", "Sand", "Tyre"]

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

print("listening on:", UDP_IP, ":", UDP_PORT)

while True:
    data, addr = sock.recvfrom(MAX_PACKET_SIZE)
    bytes = bytearray(data)

    hasIdentifier = KartKraft.Frame.Frame.FrameBufferHasIdentifier(bytes, 0)

    if hasIdentifier == False:
        continue

    frame = KartKraft.Frame.Frame.GetRootAsFrame(bytes, 0)

    if frame:
        print("\nreceived telemetry frame of size ", len(bytes), " from ", addr)
        time = frame.Timestamp()
        motion = frame.Motion()
        dash = frame.Dash()
        session = frame.Session()
        vehicleConfig = frame.VehicleConfig()
        trackConfig = frame.TrackConfig()

        print("time ", time)

        if motion:
            print("  motion data:")
            print("    angles ", motion.Pitch(),
                  motion.Roll(), motion.Yaw())
            print("    angularVel ", motion.AngularVelocityX(),
                  motion.AngularVelocityY(), motion.AngularVelocityZ())
            print("    vel ", motion.VelocityX(),
                  motion.VelocityY(), motion.VelocityZ())
            print("    accel ", motion.AccelerationX(),
                  motion.AccelerationY(), motion.AccelerationZ())
            print("    worldVel ", motion.WorldVelocityX(),
                  motion.WorldVelocityY(), motion.WorldVelocityZ())
            print("    tractionLoss ", motion.TractionLoss())
            for i in range(motion.WheelsLength()):
                print("    wheel ", i, ": surface ", SURFACE_NAMES[motion.Wheels(
                    i).Surface()], " slipAngle ", motion.Wheels(i).SlipAngle())

        if dash:
            print("  dash data:")
            print("    rpm ", dash.Rpm())
            print("    speed ", dash.Speed())
            print("    steer ", dash.Steer())
            print("    throttle ", dash.Throttle())
            print("    brake ", dash.Brake())
            print("    gear ", dash.Gear())
            print("    pos ", dash.Pos())
            print("    best lap ", dash.BestLap())
            print("    current lap ", dash.CurrentLap())
            print("    last lap ", dash.LastLap())
            print("    lap count ", dash.LapCount())
            print("    sector count ", dash.SectorCount())

        if session:
            print("  session data ", session.TimeElapsed())

        if vehicleConfig:
            print("  vehicleConfig data:")
            print("    rpm limit ", vehicleConfig.RpmLimit())
            print("    rpm max ", vehicleConfig.RpmMax())
            print("    gear max ", vehicleConfig.GearMax())

        if trackConfig:
            print("  trackConfig data:")
            if (trackConfig.Name()):
                print("    name ", str(trackConfig.Name(), "utf-8"))
            print("    numSectors ", trackConfig.NumSectors())
