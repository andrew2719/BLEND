import asyncio
import select_file
import chunker
from Commons.logger import client_logger as clog
import ed_s
class Client:
    def __init__(self):
        self.servers = {
        'server1': ('127.0.0.1', 8881),
        'server2': ('127.0.0.1', 8882),
        'server3': ('127.0.0.1', 8883),
        'server4': ('127.0.0.1', 8884),
    }
        self.connections = {}
        self.serialized_data = None
        self.sending = None
        self.distribution_table = {}



class Connections(Client):
    def __init__(self):
        super().__init__()
    async def establish_connection(self,server_ip,server_port):
        reader, writer = await asyncio.open_connection(server_ip, server_port)
        clog.info(f"Connected to {server_ip}:{server_port}")
        self.connections[server_ip] = (reader,writer)
    async def establish_connections(self):
        for server, (ip, port) in self.servers.items():
            await self.establish_connection(ip,port)

class DistributeData(Connections):
    pass
    '''
    sending request type
    {
        'type':'upload',
        'data':{
            'filename': filename,
            'size': size,

        }
    }

    after ack send data
    {'data':data}

    acknowledgement type
    {'data hash': hash}

    if true
    {'status':'save/true'}

    again wait for ack
    {'saved/not': true/false}


    else
    {'status':'false'}
    '''


class File:
    def __init__(self):
        pass
    async def process_file(self):
        file_details = await self.select_file()
        chunk_dict = await self.chunk_data(file_details)
        file_details['data'] = chunk_dict
        # clog.info(f"file details: {file_details}")
        serialized_data = await ed_s.serialize(file_details)
        # clog.info(f"serialized details: {serialized_data}")
        return serialized_data


    async def select_file(self):
        clog.info("Selecting file from system")
        file_details = await select_file.main()
        clog.info("File selected")
        return file_details

    async def chunk_data(self,data):
        clog.info("Chunking data")
        chunk_dict = await chunker.chunk(data)
        clog.info("Data chunked")
        return chunk_dict

# simple file test
client = File()
asyncio.run(client.process_file())


class ClientOperations(Connections,File):
    def __init__(self):
        super().__init__()
    async def setup(self):
        await self.establish_connections()
        await self.process_file()
        # await self.send_data()

    async def send_data(self):
        for server, (reader, writer) in self.connections.items():
            writer.write("Hello from client".encode())
            await writer.drain()
            data = await reader.read(100)
            print(f"Received: {data.decode()}")
            writer.close()
