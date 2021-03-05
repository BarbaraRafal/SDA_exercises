from typing import Optional
import requests


def get_content_from_google(status_code: int) -> Optional[str]:
    """This method is used to help understanding mocks"""
    if status_code == 200:
        return f"OK, status: {status_code}"
    elif status_code == 400:
        return f"Client error, status: {status_code}"
    elif status_code == 500:
        return f"Google is down :/ , status: {status_code}"


def get_response_status_code():
    response = requests.get("https://www.google.com")
    return response.status_code
