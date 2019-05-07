using System;
using System.Net;
using System.Net.Sockets;
using FlatBuffers;

namespace TelemetryExample
{
    class Program
    {
        static readonly int port = 5000;
        static IPEndPoint endPoint;
        static UdpClient socket;
        static AsyncCallback callback;

        static void Main(string[] args)
        {       
            //Create endpoint, socket and callback
            endPoint = new IPEndPoint(IPAddress.Any, port);
            socket = new UdpClient(endPoint);
            callback = new AsyncCallback(OnPacketReceived);

            //Wait for UDP packet to arrive
            socket.BeginReceive(callback, socket);
            Console.WriteLine("Listening on port " + port);

            while(true)
            {
                //This example app does nothing but loop forever
            }
        }

        static void OnPacketReceived(IAsyncResult result)
        {
            //Get data and retrieve TelemetryFrame
            byte[] message = socket.EndReceive(result, ref endPoint);
            ByteBuffer b = new ByteBuffer(message);
            KartKraft.Frame frame = KartKraft.Frame.GetRootAsFrame(b);

            Console.WriteLine("Received frame of length " + message.Length);

            //Handle Motion
            if (frame.Motion.HasValue)
            {
                Console.WriteLine("    motion: " + frame.Motion.Value.Pitch 
                    + " " + frame.Motion.Value.Roll 
                    + " " + frame.Motion.Value.Yaw
                    + " " + frame.Motion.Value.AccelerationX
                    + " " + frame.Motion.Value.AccelerationY
                    + " " + frame.Motion.Value.AccelerationZ);
            }

            //Handle Dashboard
            if (frame.Dash.HasValue)
            {
                Console.WriteLine("    dash: " + frame.Dash.Value.Speed
                    + " " + frame.Dash.Value.Rpm
                    + " " + frame.Dash.Value.Steer
                    + " " + frame.Dash.Value.Throttle
                    + " " + frame.Dash.Value.Brake
                    + " " + frame.Dash.Value.Gear
                    + " " + frame.Dash.Value.Pos
                    + " " + frame.Dash.Value.BestLap);
            }

            //Handle Session
            if (frame.Session.HasValue)
            {
                Console.WriteLine("    session:" + " ");
            }

            //Schedule the next receive operation
            socket.BeginReceive(callback, socket);
        }
    }
}
