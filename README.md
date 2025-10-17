# Ballot-Master

A Python program to automate the balloting process on the UNILAG student portal.

## Description

This project provides a script to automate the process of reserving accommodation for multiple users on the University of Lagos student portal. It uses a concurrent approach to handle multiple users, making the process faster and more efficient.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Tech-Mate-Ng/Ballot-Master.git
    cd Ballot-Master
    ```

2.  **Run the setup script:**

    This script will install all the necessary dependencies, including Python, pip, and Poetry, and set up the project environment.

    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```

## Configuration

After running the setup script, a `.env` file will be created in the project's root directory. You need to populate this file with the user credentials and other required information.

The format for the environment variables is as follows:

```
NUMBER_OF_USERS=2

USER1_USERNAME="matric_number_1"
USER1_PASSWORD="password_1"
USER1_HALL="hall_name_1"
USER1_DAY="day_of_ballot_1"

USER2_USERNAME="matric_number_2"
USER2_PASSWORD="password_2"
USER2_HALL="hall_name_2"
USER2_DAY="day_of_ballot_2"
```

-   `NUMBER_OF_USERS`: The total number of users you want to process.
-   `USER{i}_USERNAME`: The matriculation number for user `i`.
-   `USER{i}_PASSWORD`: The password for user `i`.
-   `USER{i}_HALL`: The desired hall of residence for user `i`. The available options are:
    -   "Mariere Hall"
    -   "Moremi Hall"
    -   "Fagunwa Hall"
    -   "Jaja Hall"
    -   "Kofo Hall"
    -   "Makama Hall"
    -   "Sodeinde Hall"
    -   "Eni Njoku Hall"
-   `USER{i}_DAY`: The day of the month scheduled for the user's balloting (e.g., `01`, `15`, `23`).

## Usage

Once the installation and configuration are complete, you can run the script using Poetry:

```bash
poetry run python main.py
```

The script will log its progress in the `log.txt` file.

## File Structure

```
.
├── credentials.py
├── depsetup.sh
├── download_utils.py
├── envsetup.sh
├── LICENSE
├── logger.py
├── main.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── setup.sh
└── user_processor.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
