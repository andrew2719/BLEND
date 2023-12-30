import aiosqlite
import asyncio
class SqliteDB:
    def __init__(self, db_path):
        self.db_path = db_path

    async def setup(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute('''CREATE TABLE IF NOT EXISTS communications 
                                (server_id TEXT, data_sent TEXT, response_received TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
            await db.commit()

    async def insert_communication(self, server_id, data_sent, response_received):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("INSERT INTO communications (server_id, data_sent, response_received) VALUES (?, ?, ?)",
                             (server_id, data_sent, response_received))
            await db.commit()

    async def fetch_all_communications(self):
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("SELECT * FROM communications")
            rows = await cursor.fetchall()
            return rows

# obj = SqliteDB('test.db')
# asyncio.run(obj.setup())
# asyncio.run(obj.insert_communication('server1', 'Hello, Server!', 'Data received'))
# asyncio.run(obj.insert_communication('server2', 'Hello, Server!', 'Data received'))