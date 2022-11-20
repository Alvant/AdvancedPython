import asyncio
import time

from typing import Awaitable, List

import aiohttp

from constants import IO_SITES
from utils import show_execution_time


async def download_site(session: aiohttp.ClientSession, url: str) -> Awaitable[None]:
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url}")


async def download_all_sites(sites: List[str]) -> Awaitable[None]:
    async with aiohttp.ClientSession() as session:
        tasks = list()
        
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    show_execution_time(
        func=lambda: loop.run_until_complete(download_all_sites(IO_SITES))
    )

    loop.close()
