import multiprocessing
import time

from typing import List, Optional

import requests

from constants import IO_SITES
from utils import show_execution_time


session: Optional[requests.Session] = None


def set_global_session() -> None:
    global session

    if session is None:
        session = requests.Session()


def download_site(url: str) -> None:
    with session.get(url) as response:
        process_name = multiprocessing.current_process().name

        print(f"{process_name}:Read {len(response.content)} from {url}")


def download_all_sites(sites: List[str]) -> None:
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    show_execution_time(func=lambda: download_all_sites(IO_SITES))
