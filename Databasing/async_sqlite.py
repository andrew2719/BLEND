import aiosqlite
import asyncio
class SqliteDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
    #     store the connection to a varaible and use it in all the methods
    #     self.connection = await aiosqlite.connect(self.db_path)

    async def create_table(self,query):
        await self.connection.execute(query)
        await self.connection.commit()


    async def setup(self):
        self.connection = await aiosqlite.connect(self.db_path)
        # create server table
        await self.create_table("CREATE TABLE IF NOT EXISTS servers (server_ip TEXT, hash TEXT)")
        # file table




class Clinet_operations(SqliteDB):
    def __init__(self, db_path):
        super().__init__(db_path)
        self.client_connection = None

    async def connect(self):
        await super().setup()
        self.client_connection = await aiosqlite.connect(self.db_path)
    async def insert_server(self,server_ip,hash):
        pass

    async def file_data(self,**kwargs):
        file_name = kwargs.get("file_name")
        extension = kwargs.get("extension")
        hash = kwargs.get("hash")
        size = kwargs.get("size")
