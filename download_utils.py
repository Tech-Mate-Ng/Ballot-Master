#!/usr/bin/env python
"""
This module provides utility functions for downloading files and data from URLs.
"""
import base64
import requests
import logging


def download_file(url, filename):
    """
    Downloads a file from the given URL and saves it with the specified filename.

    Args:
            url (str): The URL of the file to download.
            filename (str): The name of the file to save.

    Returns:
            None
    """
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)
    logging.info(f"Downloaded file: {filename}")


def download_data_url(url, filename):
    """
    Downloads data from a data URL and saves it with the specified filename.

    Args:
            url (str): The data URL.
            filename (str): The name of the file to save.

    Returns:
            None
    """
    header, data = url.split(",", 1)
    file_data = base64.b64decode(data)
    with open(filename, "wb") as file:
        file.write(file_data)
    logging.info(f"Downloaded data from URL: {url}")
