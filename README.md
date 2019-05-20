# KartKraft UPD Data Transfer

KartKraft outputs UDP packets for motion rig control, telemetry dashboards and game session data. This repository contains example code to help you get up and running fast.

## Simple Examples

We include everything you need to write your own plugin in a variety of languages. Check out the examples to see how easy it is, and how to structure your code.

### Python

- `ListenForTelemetry.py` : Example telemetry receiver. Writes out any data received.
- `SendTelemetry.py` : Handy testing tool. Invoking this will send a single example telemetry frame.
- To write your own app/plugin, you'll need all code contained in the `flatbuffers` and `kartkraft` folders.

### Cpp

- `ListenForTelemetry.sln` : A Windows/winsock2 VS2017 example is provided though serialization principles are cross-platform and will work with multiple compilers.
- To write your own app/plugin, you'll need all code contained in the `Flatbuffers` and `KartKraft` folders.

### CSharp

- `ListenForTelemetry.sln` : A .NET framework 3.5 example suitable for Windows/Unity. All code is also compatible with .NET Core should you wish to use it in Linux/Mac/Windows applications.
- To write your own app/plugin, you'll need all code contained in the `Flatbuffers` and `KartKraft` folders.

### Java

- `ListenForTelemetry.java` : Example telemetry receiver. Writes out any data received.
- To write your own app/plugin, you'll need all code contained in the `com/google/flatbuffers` and `KartKraft` folders.

### Javascript

- `ListenForTelemetry.js` : A simple `Node.js` telemetry receiver example.
- To write your own app/plugin, you'll need all code contained in the `flatbuffers` and `kartkraft` folders.

## Example Electron Telemetry Chart App

We provide a [basic realtime telemetry charting app](https://github.com/black-delta/kartkraft-telemetry/tree/master/Examples/Electron) written using the Electron framework in javascript. Feel free to fork this and use as the basis of your own simple app.

## Schema

We utilize a technology called Flatbuffers to formally define the format of UDP packets. This format will evolve over time, adding new features without breaking backwards compatibility. The current schema is defined in [Frame.fbs](https://github.com/black-delta/kartkraft-telemetry/blob/master/Schema/Frame.fbs)

Benefits of using Flatbuffers include:

- Automatic serialization/deserialization code, meaning plugins don't need to write any code to decode packets manually.
- Reading data from received packets can be performed without memory allocation, allowing for high performance code and higher frequency packet sending.
- Forwards/backwards compatibility: Fields can be deprecated and new or missing fields will not crash existing serialization code.
- Support for multiple languages. If your favorite language isn't included in the list below, let us know and we may be able to add it.
- The format of UDP packets is specified in a formalized, testable way. (See Frame.fbs)

For reference, we are currently using this release of Flatbuffers to generate the code in this repository.
https://github.com/google/flatbuffers/releases/tag/v1.10.0

## Auto-patching KartKraft

If you wish to avoid the preferences menu you can patch the telemetry setup via ini file. Using this method will also let you add as many IP address targets as you wish.

You will need to edit `Game.ini` which can usually be located here:

`%localappdata%\project_k\Saved\Config\WindowsNoEditor\Game.ini`

#### Example ini file setup

Adding the following lines to `Game.ini` will override the preferences menu, target two devices at different IP addresses, and enable standard UDP output.

```
[/Script/project_k.UDPManager]
bConfigOverride=True
OutputEndpoints="127.0.0.1:5000"
OutputEndpoints="10.0.0.1:5001"
bEnableOutputStandard=True
```
