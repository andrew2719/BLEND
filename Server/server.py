import asyncio

async def handle_client(reader, writer):
    data = await reader.read(100)
    print(f"Received: {data.decode()}")

    response = 'Data received'
    writer.write(response.encode())
    await writer.drain()

    writer.close()

async def ajay():
    pass
async def main():
    port = 8881  # Change this for each server
    server = await asyncio.start_server(handle_client, '127.0.0.1', port)
    await server.serve_forever()

asyncio.run(main())
