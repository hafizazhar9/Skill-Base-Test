#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int client_socket;
    struct sockaddr_in server_address;
    int random_num;

    // create client socket
    client_socket = socket(AF_INET, SOCK_STREAM, 0);

    // configure server address
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(8080);
    server_address.sin_addr.s_addr = inet_addr("192.168.150.131");

    // connect to server
    connect(client_socket, (struct sockaddr *) &server_address, sizeof(server_address));

    // receive random number from server
    recv(client_socket, &random_num, sizeof(random_num), 0);

    // print received random number
    printf("Random number that has been received: %d\n", random_num);

    // close client socket
    close(client_socket);

    return 0;
}