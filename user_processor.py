#!/usr/bin/env python3
"""
This script processes user data and makes accommodation reservations for eligible users.
"""

import time
import json
import logging
import requests
from credentials import get_credentials


def process_user(i):
    """
    Process a user's accommodation reservation.

    Args:
            i (int): The user's identifier.

    Returns:
            None

    Raises:
            None
    """
    username, password, hall, day = get_credentials(i)
    if day != time.strftime("%d"):
        logging.info("Skipping user %d as it is not their day", i)
        logging.info("Day: %s Current Day: %s", day, time.strftime("%d"))
        return

    base_url = "http://studentportalbeta.unilag.edu.ng/"
    hall_id_dict = {
        "Mariere Hall": "MARIERE%20HALL",
        "Moremi Hall": "MOREMI%20HALL",
        "Fagunwa Hall": "FAGUNWA%20HALL",
        "Jaja Hall": "JAJA%20HALL",
        "Kofo Hall": "KOFO%20HALL",
        "Makama Hall": "MAKAMA%20HALL",
        "Sodeinde Hall": "SODEINDE%20HALL",
        "Eni Njoku Hall": "ENI%20NJOKU%20HALL",
    }

    with requests.Session() as s:
        response = s.post(
            f"{base_url}users/login",
            data={"MatricNo": username, "Password": password},
        )
        if response.status_code != 200:
            logging.error("Failed to login user %d", i)
            return
        logging.info(
            "Successfully logged in %s",
            json.loads(response.text)["Data"]["Student"]["FullName"],
        )

        s.cookies["_auth"] = response.text
        general_header = {
            "Authorization": f"Bearer {json.loads(response.text)['Data']['Token']}",
            "Content-Type": "application/json",
            "Host": "studentportalbeta.unilag.edu.ng",
            "Referer": "http://studentportal.unilag.edu.ng/",
        }

        response = s.get(
            f"{base_url}accomodation/accomodationHalls",
            headers=general_header,
        )
        logging.info("Response from accomodationHalls: %s", response.text)

        res = json.dumps({"HallId": hall_id_dict[hall]})
        response = s.post(
            f"{base_url}accomodation/saveAccommodationReservation",
            data=res,
            headers=general_header,
        )
        logging.info(
            "Response from saveAccommodationReservation: %s", response.text
        )
