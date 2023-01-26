import asyncio

async def main():
    host = "172.20.10.11"
    port = 8080

    reader, writer = await asyncio.open_connection(host, port)
    print(f"[*] Connected to {host}:{port}")

    while True:
        fahrenheit = input("Enter temperature in Fahrenheit: ")
        if not fahrenheit:
            break

        writer.write(fahrenheit.encode())
        await writer.drain()

        celsius = await reader.read(1024)
        celsius = celsius.decode()
        print(f"The temperature in Celsius: {celsius}")

    writer.close()

if __name__ == "__main__":
    asyncio.run(main())
