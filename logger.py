#!/usr/bin/env python3
"""
This module provides functions for configuring the logging system.
"""
import logging


def configure_logging():
    """
    Configures the logging settings.

    This function sets up the logging module with the specified settings.
    It configures the log file path, log level, and log message format.

    Args:
            None

    Returns:
            None
    """
    logging.basicConfig(
        filename="log.txt",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
