import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class AutoFill:
    def __init__(self):
        self.radio_id = [
            ["i9", "i12", "i15", "i18"],
            ["i25", "i28", "i31"]
        ]
        self.checkbox_id = [
            ["i39", "i42", "i45"]
        ]
        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
