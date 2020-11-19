import time

from typing import Callable


def show_execution_time(func: Callable[[], None]) -> None:
    start_time = time.time()
    
    func()

    duration = time.time() - start_time

    print(f"\nDuration: {duration} seconds")
