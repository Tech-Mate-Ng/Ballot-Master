#!/usr/bin/env python3
"""
This script is the main entry point for processing user data.
It uses a ThreadPoolExecutor to process user data concurrently.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
from user_processor import process_user
from logger import configure_logging
import os


def main():
    """
    Entry point of the program.
    """
    configure_logging()

    number_of_users = int(os.getenv("NUMBER_OF_USERS"))
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(process_user, i)
            for i in range(1, number_of_users + 1)
        ]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
