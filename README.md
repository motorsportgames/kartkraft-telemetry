# KartKraft UPD data transfer

KartKraft outputs UDP packets for motion rig control, telemetry dashboards (coming soon) and game session data (coming soon).

## Flatbuffers

We utilize a technology called Flatbuffers. Benefits of using this library include:

- automatic serialization/deserialization code (plugins don't need to write any code to decode packets manually)
- reading data from received packets does not require memory allocation, allowing for high performance code and higher frequency packet sending.
- forwards/backwards compatibility (fields can be deprecated, new or missing fields will not crash existing serialization code)
- support for multiple languages (if your favourite language isn't included in the list below, let us know and we may be able to add it)
- the format of udp packets is specified in a formalised, testable way. (.fbs file)

For refernece, we are currently using this release of Flatbuffers to generate the code in this repository.
https://github.com/google/flatbuffers/releases/tag/v1.10.0

## Supported Languages

We include everything you need to write your own plugin in a variety of languages. Check out the examples to see how easy it is, and how to structure your code.

### Python

- Python listening example
- Python sending example
- Location of flatbuffers files
- Location of telemtry header file

### Cpp

- Windows/winsock2 VS2017 example is provided though serialization principles are crossplatform
- Location of flatbuffers files
- Location of telemetry header file

### CSharp

- Solution containing .net 3.5 (Windows/Unity) and .net core 2.0 (Win/Mac/Linux) projects
- Location of flatbuffers dll
- Location of telemetry header file

### Java

- Location of flatbuffers dll
- Location of telemetry header file

### Javascript

- Node example provided
- Location of flatbuffers files
- Location of telemetry header file
