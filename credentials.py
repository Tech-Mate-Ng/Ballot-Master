#!/usr/bin/env python3
"""
This module provides functions for retrieving user credentials.

Functions:
- get_credentials(i): Returns the username, password, hall, and day for a given user index.
"""

import os
from dotenv import load_dotenv

load_dotenv(override=True)


def get_credentials(i):
    """
    Returns the username, password, hall, and day for a given user index.

    Args:
    - i (int): The index of the user.

    Returns:
    - tuple: A tuple containing the username, password, hall, and day for the user.
    """
    return (
        os.getenv(f"USER{i}_USERNAME"),
        os.getenv(f"USER{i}_PASSWORD"),
        os.getenv(f"USER{i}_HALL"),
        os.getenv(f"USER{i}_DAY"),
    )
