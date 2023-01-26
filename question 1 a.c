#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
    int server_socket, client_socket, random_num;
    struct sockaddr_in server_address, client_address;
    int client_address_len = sizeof(client_address);

    // create server socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);

    // configure server address
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(8080);
    server_address.sin_addr.s_addr = INADDR_ANY;

    // bind server socket to address
    bind(server_socket, (struct sockaddr *) &server_address, sizeof(server_address));

    // listen for incoming connections
    listen(server_socket, 5);

    while (1) {
        // accept incoming connection
        client_socket = accept(server_socket, (struct sockaddr *) &client_address, &client_address_len);

        // generate random number between 100 and 999
        srand(time(0));
        random_num = rand() % 900 + 100;

        // send random number to client
        send(client_socket, &random_num, sizeof(random_num), 0);


    }


    return 0;
}