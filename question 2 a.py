import asyncio

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

async def handle_connection(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f"[*] Connection from {addr}")

    while True:
        data = await reader.read(1024)
        if not data:
            break
        data = data.decode()
        print(f"[*] Received {data} from {addr}")

        celsius = fahrenheit_to_celsius(float(data))
        writer.write(str(celsius).encode())
        await writer.drain()
        print(f"[*] Sent {celsius} to {addr}")

    writer.close()

async def main():
    host = "172.20.10.11"
    port = 8080

    server = await asyncio.start_server(handle_connection, host, port)
    addr = server.sockets[0].getsockname()
    print(f"[*] Listening on {addr}")

    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
