import asyncio
import aiohttp
import socket

async def test_dns():
    print("--- DNS Diagnostic ---")
    host = "discord.com"
    try:
        addrinfo = socket.getaddrinfo(host, 443)
        print(f"✅ socket.getaddrinfo working: {addrinfo[0][4][0]}")
    except Exception as e:
        print(f"❌ socket.getaddrinfo failed: {e}")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://{host}") as resp:
                print(f"✅ aiohttp connection successful: Status {resp.status}")
    except Exception as e:
        print(f"❌ aiohttp failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_dns())
