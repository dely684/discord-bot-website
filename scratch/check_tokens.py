import asyncio
import aiosqlite

DB_PATH = 'bot_database.db'

async def check():
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute("SELECT *, length(token) as len FROM tokens")
        rows = await cursor.fetchall()
        for row in rows:
            print(dict(row))

if __name__ == "__main__":
    asyncio.run(check())
