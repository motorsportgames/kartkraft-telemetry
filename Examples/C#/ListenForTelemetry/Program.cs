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

            if (KartKraft.Frame.FrameBufferHasIdentifier(b))
            { 
                KartKraft.Frame frame = KartKraft.Frame.GetRootAsFrame(b);

                Console.WriteLine("Received frame of length " + message.Length);

                //Handle Motion
                if (frame.Motion.HasValue)
                {
                    Console.WriteLine("  motion data:");
                    Console.WriteLine("    angles {0} {1} {2}", frame.Motion.Value.Pitch, frame.Motion.Value.Roll, frame.Motion.Value.Yaw);
                    Console.WriteLine("    angularVel {0} {1} {2}", frame.Motion.Value.AngularVelocityX, frame.Motion.Value.AngularVelocityY, frame.Motion.Value.AngularVelocityZ);
                    Console.WriteLine("    vel {0} {1} {2}", frame.Motion.Value.VelocityX, frame.Motion.Value.VelocityY, frame.Motion.Value.VelocityZ);
                    for(int i=0; i < frame.Motion.Value.WheelsLength; i++)
                    {
                        if (frame.Motion.Value.Wheels(i).HasValue)
                        {
                            KartKraft.Wheel wheel = frame.Motion.Value.Wheels(i).Value;
                            Console.WriteLine("    wheel {0} surface {1} slipAngle {2} ", i, wheel.Surface, wheel.SlipAngle);
                        }
                    }

                }

                //Handle Dashboard
                if (frame.Dash.HasValue)
                {
                    Console.WriteLine("  dash data:");
                    Console.WriteLine("    rpm {0}", frame.Dash.Value.Rpm);
                    Console.WriteLine("    speed {0}", frame.Dash.Value.Speed);
                    Console.WriteLine("    steer {0}", frame.Dash.Value.Steer);
                    Console.WriteLine("    throttle {0}", frame.Dash.Value.Throttle);
                    Console.WriteLine("    brake {0}", frame.Dash.Value.Brake);
                    Console.WriteLine("    gear {0}", frame.Dash.Value.Gear);
                    Console.WriteLine("    pos {0}", frame.Dash.Value.Pos);
                    Console.WriteLine("    best lap {0}", frame.Dash.Value.BestLap);
                    Console.WriteLine("    current lap {0}", frame.Dash.Value.CurrentLap);
                    Console.WriteLine("    last lap {0}", frame.Dash.Value.LastLap);
                    Console.WriteLine("    lap count {0}", frame.Dash.Value.LapCount);
                }

                //Handle Session
                if (frame.Session.HasValue)
                {
                    Console.WriteLine("    session:" + " ");
                }
            }

            //Schedule the next receive operation
            socket.BeginReceive(callback, socket);
        }
    }
}
