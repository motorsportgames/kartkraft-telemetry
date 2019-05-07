import java.net.DatagramSocket;
import java.net.DatagramPacket;
import java.nio.ByteBuffer;

public class ListenForTelemetry {

    private static DatagramSocket socket;
    private static int port = 5000;
    private static byte[] buffer = new byte[1024];
    private static Boolean listening;

    public static void main(String[] args) throws Exception {

        // Create socket
        socket = new DatagramSocket(port);
        System.out.println("Listening on port " + port + "...");

        // Start listening
        listening = true;
        while (listening) {

            // Construct new packet, reuse the buffer
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);

            // Receive the packet and try converting to kartkraft Frame
            socket.receive(packet);
            ByteBuffer byteBuffer = ByteBuffer.wrap(buffer);
            KartKraft.Frame frame = KartKraft.Frame.getRootAsFrame(byteBuffer);

            if (frame != null) {

                System.out.println("Received frame of length " + packet.getLength());

                KartKraft.Motion motion = frame.motion();
                KartKraft.Dashboard dash = frame.dash();
                KartKraft.Session session = frame.session();

                // Handle motion data
                if (motion != null) {
                    System.out.println("    motion: " + motion.pitch() + " " + motion.roll() + " " + motion.yaw() + " "
                            + motion.accelerationX() + " " + motion.accelerationY() + " " + motion.accelerationZ() + " "
                            + motion.tractionLoss());
                }

                // Handle dashboard data
                if (dash != null) {
                    System.out.println(
                            "    dash: " + dash.speed() + " " + dash.rpm() + " " + dash.steer() + " " + dash.throttle()
                                    + " " + dash.brake() + " " + dash.gear() + " " + dash.pos() + " " + dash.bestLap());
                }

                // Handle session data
                if (session != null) {
                    System.out.println("    session: ");
                }
            }
        }

        socket.close();
    }
}