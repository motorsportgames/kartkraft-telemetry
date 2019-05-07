#include <iostream>
#include <WinSock2.h>
#include "Flatbuffers/flatbuffers.h"
#include "KartKraft/Frame_generated.h"

const int PORT = 5000;
const int BUFFER_SIZE = 1024;

int main()
{
	//Start up winsock
	WSADATA winsockData;
	if (WSAStartup(MAKEWORD(2, 2), &winsockData) != 0)
	{
		printf("Server: WSAStartup failed with error %ld\n", WSAGetLastError());
		return -1;
	}

	//Create socket
	SOCKET receiver = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
	if (receiver == INVALID_SOCKET)
	{
		printf("Failed to create socket!");
		WSACleanup(); 
		return -1;
	}

	//Bind socket to port 
	sockaddr_in socketAddress;
	socketAddress.sin_family = AF_INET;
	socketAddress.sin_port = htons(PORT);
	socketAddress.sin_addr.s_addr = htonl(INADDR_ANY);

	int bindResult = bind(receiver, (sockaddr *)&socketAddress, sizeof(socketAddress));
	if (bindResult < 0)
	{
		printf("Failed to bind socket!");
		WSACleanup(); // Clean up
		return -1;
	}

	//Wait for messages in a loop
	char buffer[BUFFER_SIZE];
	sockaddr senderAddress;
	int senderAddressLength = sizeof(senderAddress);

	while (true) 
	{
		printf("Listening on port %d...\n", PORT);

		//App blocks and waits here for next message to come through
		int receivedLength = recvfrom(receiver, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&senderAddress, &senderAddressLength);
		if (receivedLength > 0) 
		{		
			const KartKraft::Frame * frame = KartKraft::GetFrame(buffer);
			if (frame)
			{
				printf("Received frame of length %d\n", receivedLength);

				const KartKraft::Motion * motion = frame->motion();
				const KartKraft::Dashboard * dash = frame->dash();
				const KartKraft::Session * session = frame->session();

				//Handle motion data
				if (motion)
				{
					printf("    motion: %f %f %f %f %f %f %f\n", 
						motion->pitch(), 
						motion->roll(), 
						motion->yaw(), 
						motion->accelerationX(), 
						motion->accelerationY(), 
						motion->accelerationZ(), 
						motion->tractionLoss());
				}

				//Handle dashboard data
				if (dash)
				{
					printf("    dash: %f %f %f %f %f %d %d %f\n", 
						dash->speed(), 
						dash->rpm(), 
						dash->steer(), 
						dash->throttle(), 
						dash->brake(), 
						dash->gear(), 
						dash->pos(), 
						dash->bestLap());
				}

				//Handle session data
				if (session)
				{
					printf("    session: \n\n");
				}
			}
		}
	}

	WSACleanup(); // Clean up
	return 0;
}
