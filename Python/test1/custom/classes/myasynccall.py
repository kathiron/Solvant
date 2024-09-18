import asyncio

class myasynccall:
    def __init__(self) -> None:
        # TODO document why this method is empty
        pass

    async def fetch_data(self, url):
        # Simulate an asynchronous operation (e.g., fetching data from a web API)
        await asyncio.sleep(1)
        return f"Data from {url}"

    async def callasyncmethod(self):
        data1 = await self.fetch_data("https://example.com/data1")
        data2 = await self.fetch_data("https://example.com/data2")
        print(data1)
        print(data2)
