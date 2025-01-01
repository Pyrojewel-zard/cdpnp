import asyncio

def regular_function():
    return "Hello from a regular function!"

async def async_function():
    await asyncio.sleep(1)
    return "Hello from an async function!"

print(regular_function())
print(asyncio.run(async_function()))