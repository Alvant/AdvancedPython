import time

from typing import List

import requests

from constants import IO_SITES
from utils import show_execution_time


def download_site(url: str, session: requests.Session) -> None:
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites: List[str]) -> None:
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    show_execution_time(func=lambda: download_all_sites(IO_SITES))
