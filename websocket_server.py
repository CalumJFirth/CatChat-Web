import asyncio
from websockets.asyncio.server import serve


async def handle_client(websocket):
    print("Client connected")

    try:
        message = await websocket.recv()

        print("Received:", message)

        await websocket.wait_closed()

    finally:
        print("Client disconnected")


async def main():
    async with serve(handle_client, "127.0.0.1", 8765):
        print("WebSocket server listening on ws://127.0.0.1:8765")

        await asyncio.Future()   # run forever


asyncio.run(main())