import asyncio
import aiohttp
import socket
import sys

# Diagnostic for SelectorEventLoop
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def test_dns():
    print(f"--- DNS Diagnostic (Loop: {asyncio.get_event_loop_policy().__class__.__name__}) ---")
    host = "discord.com"
    try:
        # Test synchronous resolution (should work)
        addrinfo = socket.getaddrinfo(host, 443)
        print(f"✅ socket.getaddrinfo (sync) working: {addrinfo[0][4][0]}")
    except Exception as e:
        print(f"❌ socket.getaddrinfo (sync) failed: {e}")

    try:
        # Test async resolution (this is what fails in main.py)
        loop = asyncio.get_running_loop()
        res = await loop.getaddrinfo(host, 443)
        print(f"✅ loop.getaddrinfo (async) working: {res[0][4][0]}")
    except Exception as e:
        print(f"❌ loop.getaddrinfo (async) failed: {e}")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://{host}") as resp:
                print(f"✅ aiohttp connection successful: Status {resp.status}")
    except Exception as e:
        print(f"❌ aiohttp failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_dns())
