import concurrent.futures
import threading
import time

from typing import List

import requests

from constants import IO_SITES
from utils import show_execution_time


THREAD_LOCAL = threading.local()


def get_session() -> requests.Session:
    if not hasattr(THREAD_LOCAL, "session"):
        THREAD_LOCAL.session = requests.Session()

    return THREAD_LOCAL.session


def download_site(url: str) -> None:
    session = get_session()

    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites: List[str], max_workers: int = 5) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    show_execution_time(func=lambda: download_all_sites(IO_SITES))
