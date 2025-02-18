class Config:
    BASE_URL = "https://stellarburgers.nomoreparties.site/"

    URLS = {
        "main": BASE_URL,
        "register": f"{BASE_URL}register",
        "login": f"{BASE_URL}login",
        "forgot_password": f"{BASE_URL}forgot-password",
        "profile": f"{BASE_URL}account/profile",
    }
