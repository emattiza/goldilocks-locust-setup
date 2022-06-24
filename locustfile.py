from locust import HttpUser, task
from requests import Response
from bs4 import BeautifulSoup


def findToken(base: Response) -> str:
    """
    Yeah this is no fun, but hey, we need the token
    """
    tree = BeautifulSoup(base.text, "html5lib")
    token = tree.find("input", {"type": "hidden", "name": "csrfmiddlewaretoken"})
    if token is None:
        return ""
    else:
        token = token.attrs["value"]
    return token


class BaseUser(HttpUser):
    @task
    def hello_site(self):
        """
        Story is as follows:
        1. User navigates to base url
        2. User logins
        3. User navigates to farm after successful login
        """
        base: Response = self.client.get("/")
        foundToken: str = findToken(base)
        response: Response = self.client.post(
            "/users/login/",
            {
                "username": "",
                "password": r"",
                "csrfmiddlewaretoken": foundToken,
            },
            headers={
                "Referer": base.headers.get(
                    "Referer", ""
                )
            },
            cookies=base.cookies,
        )
        if response.ok:
            self.client.get("/farms/13")
