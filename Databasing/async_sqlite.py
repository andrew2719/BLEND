import aiosqlite
import asyncio
class SqliteDB:
    def __init__(self):
        self.db_name = "BLEND"
        self.db_path = f"{self.db_name}.db"
        self.connection = None
    #     store the connection to a varaible and use it in all the methods
    #     self.connection = await aiosqlite.connect(self.db_path)

    async def connect(self):
        self.connection = await aiosqlite.connect(self.db_path)
    async def create_table(self,query):
        await self.connection.execute(query)
        await self.connection.commit()




class Clinet_operations(SqliteDB):
    def __init__(self):
        super().__init__()

    async def setup(self):
        await self.connect()
        # create server table
        await self.create_table("CREATE TABLE IF NOT EXISTS servers (server_ip TEXT, hash TEXT)")
        # file table
        await self.create_table("CREATE TABLE IF NOT EXISTS files (file_name TEXT, extension TEXT, hash TEXT, size INT, data BLOB)")



    async def file_data(self,**kwargs):
        file_name = kwargs.get("file_name")
        extension = kwargs.get("extension")
        hash = kwargs.get("hash")
        size = kwargs.get("size")
        data = kwargs.get("data")


client = Clinet_operations()
asyncio.run(client.setup())

