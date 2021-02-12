from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime
import collections
import argparse
import time
import json
import os
import re

class UdemyCrawler:
    # https://www.udemy.com/courses/search/?src=ukw&q=scala+programming+akka
    search_url = 'https://www.udemy.com/courses/search/?src=ukw&q='

    def __init__(self, keywords):
        self.url += '+'.join(keywords)


if __name__ == '__main__':

