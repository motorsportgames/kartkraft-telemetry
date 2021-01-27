extern crate flatbuffers;

use std::net::UdpSocket;

#[allow(dead_code, unused_imports)]
#[allow(non_snake_case)]
#[path = "./Frame_generated.rs"]
mod Frame_generated;
pub use Frame_generated::kart_kraft::{*};

fn main() {

    let host_address = "127.0.0.1:1234";
    let target_address = "127.0.0.1:2468";

    //Create a socket
    let socket = UdpSocket::bind(host_address).expect("Failed to bind host socket!");

    //Create flatbuffer build object in which to put data
    let mut builder = flatbuffers::FlatBufferBuilder::new_with_capacity(1024);

    //Build some example dashboard data
    let dashboard = Dashboard::create(&mut builder, &DashboardArgs{
        lastLap: 0.012,
        currentLap: 0.23,
        bestLap: 1.23,
        brake: 1.0,
        throttle: 0.56,
        steer: -0.3,
        rpm: 4250.0,
        speed: 0.0,
        sectorCount: 0,
        lapCount: 0,
        pos: 0,
        gear: 0
    });

    //Build some example motion data
    let motion = Motion::create(&mut builder, &MotionArgs{
        worldVelocityX: 1.2345,
        worldVelocityY: 2.3456,
        worldVelocityZ: 3.4567,
        accelerationX: 4.5678,
        accelerationY: 5.6789,
        accelerationZ: 6.7890,
        angularVelocityX: 7.8901,
        angularVelocityY: 8.9012,
        angularVelocityZ: 9.0123,
        pitch: 0.001,
        roll: 0.002,
        yaw: 0.003,
        velocityX: 0.004,
        velocityY: 0.005,
        velocityZ: 0.006,
        tractionLoss: 0.0,
        wheels: None
    });

    // Examples of creating default data
    // let session = Session::create(&mut builder, &SessionArgs::default());
    // let track_config = TrackConfig::create(&mut builder, &TrackConfigArgs::default());
    // let vehicle_config = VehicleConfig::create(&mut builder, &VehicleConfigArgs::default());

    let frame = Frame::create(&mut builder, &FrameArgs{
        timestamp: 0.123,
        dash: Some(dashboard),
        motion: Some(motion),
        session: None,
        trackConfig: None,
        vehicleConfig: None
    });

    //Finish the frame and get the buffer ready for sending
    finish_frame_buffer(&mut builder, frame);
    let buffer = builder.finished_data();

    //Send to target_address
    println!("\nSending {} bytes to {}...", buffer.len(), target_address);
    match socket.send_to(&buffer, target_address) {
        Ok(number_of_bytes) => print!("Successfully sent {} bytes.", number_of_bytes),
        Err(fail) => println!("Failed sending {:?}", fail),
    }
}

