use std::net::UdpSocket;

#[allow(dead_code, unused_imports)]
#[allow(non_snake_case)]
#[path = "../../kartkraft/Frame_generated.rs"]
mod Frame_generated;
pub use Frame_generated::kart_kraft::{*};

fn main() -> std::io::Result<()> {

    let host_address = "127.0.0.1:5000";

    //Create a socket
    let socket = UdpSocket::bind(host_address)?;
    println!("\nListening on {}...\n", host_address);
    
    //Create a buffer to read data in to
    let mut buf = [0; 512];

    //Loop and listen for udp packets
    loop {
        
        //Wait for next message to arrive
        let (byte_count, src) = socket.recv_from(&mut buf)?;    

        //Only process this frame if the identifier is present (this is the minimal amount of verification possible to protect against other data received on this port)
        if frame_buffer_has_identifier(&buf) {

            println!("\nReceived a frame containing {} bytes from {}", byte_count, src);

            let frame = get_root_as_frame(&buf);
            
            //Timestamp (always present)
            println!("\nTimestamp: {}", frame.timestamp());
            
            //Dashboard (cehcek if exists)
            println!("\nDashboard:");
            if let Some(dash) = frame.dash() {
                println!("  Throttle:         {}", dash.throttle());
                println!("  Brake:            {}", dash.brake());
                println!("  Steer:            {}", dash.steer());
                println!("  RPM:              {}", dash.rpm());
            } else {
                println!("  (No dashboard data received)");
            }

            //Motion (cehcek if exists)
            println!("\nMotion:");
            if let Some(motion) = frame.motion() {                
                println!("  Local velocity:   ({}, {}, {})", motion.velocityX(), motion.velocityY(), motion.velocityZ());
                println!("  World velocity:   ({}, {}, {})", motion.worldVelocityX(), motion.worldVelocityY(), motion.worldVelocityZ());
                println!("  Angular velocity: ({}, {}, {})", motion.angularVelocityX(), motion.angularVelocityY(), motion.angularVelocityZ());
                println!("  Angle:            ({}, {}, {})", motion.pitch(), motion.roll(), motion.yaw());
                println!("  Traction loss:    {}", motion.tractionLoss());
            } else {
                println!("  (No motion data received)");
            }

            //Session
            //...

            //TrackConfig
            //...

            //VehicleConfig
            //...
        }
    }
}
