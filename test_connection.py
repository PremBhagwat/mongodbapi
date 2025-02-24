from db import database
import asyncio

async def check_connection():
    try:
        collections = await database.list_collection_names()
        print(f"Connected! Collections: {collections}")
    except Exception as e:
        print(f"Connection Failed: {e}")

asyncio.run(check_connection())
