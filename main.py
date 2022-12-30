from news_api import search_and_return
from sms_send import send_sms


def search_term():
    """Get search term from user."""
    while True:
        try:
            user_search = input("What top current articles category would you like to search? ")
            confirm = input(f"Are you sure you want to search for {user_search}? (y/n) ")
            if confirm.lower() == "y":
                results = search_and_return(user_search)
                break
            elif confirm.lower() == "n":
                continue
            else:
                raise ValueError("Invalid response. Please enter 'y' or 'n'.")
        except ValueError as error:
            print(error)
    return results


def send_text(message):
    """Send text message to user."""
    while True:
        try:
            user_phone = input("What is your phone number, with country code? ")
            confirm = input(f"Is {user_phone} correct? (y/n) ")
            if confirm.lower() == "y":
                phone = user_phone
                print("Sending text message...")
                send_sms(message, phone)
                break
            elif confirm.lower() == "n":
                continue
            else:
                raise ValueError("Invalid response. Please enter 'y' or 'n'.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    message = search_term()
    send_text(message)
