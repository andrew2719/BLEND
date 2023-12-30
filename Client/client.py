import asyncio


async def communicate_with_server(server_ip, server_port, data_to_send, communication_record):
    reader, writer = await asyncio.open_connection(server_ip, server_port)
    writer.write(data_to_send.encode())
    await writer.drain()

    response = await reader.read(100)
    communication_record[server_ip] = response.decode()

    writer.close()


async def main():
    servers = {
        'server1': ('127.0.0.1', 8881),
        'server2': ('127.0.0.1', 8882),
        'server3': ('127.0.0.1', 8883),
        'server4': ('127.0.0.1', 8884),
    }

    data_to_send = "Hello, Server!"
    communication_record = {}

    # Create a list of tasks, one for each server
    tasks = []
    for server, (ip, port) in servers.items():
        task = communicate_with_server(ip, port, data_to_send, communication_record)
        tasks.append(task)

    # Run all the tasks concurrently
    await asyncio.gather(*tasks)

    # Print the communication record
    for server, response in communication_record.items():
        print(f"Data sent to {server} received response: {response}")


asyncio.run(main())
