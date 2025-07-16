from getpass import getpass
import logging
logger = logging.getLogger(__name__)

def setup():
    username = ""
    password = ""
    age = ""
    try:

        username = input("Username: ")
        password = password = getpass("Password: ")

        try: 
            age = int(input("Age: "))
        except ValueError as age_error:
            logger.info(f"Invalid input: {age_error}. \
                Expecting an integer.")

    except Exception as outer_error:
        logger.info(f"Unexpected error: {outer_error}")

    return username, password, age

def display(**kwargs):
    logger.info("Displaying parameters: ")
    for key, value in kwargs.items():
        logger.info(f"\t{key}: {value}")

if __name__ == "__main__":
    username = ""
    password = ""
    age = ""
    while not username or not password or not age: 
        print("Input a valid username, password and age.")
        username, password, age = setup()

    display(username=username, password=password, age=age)


