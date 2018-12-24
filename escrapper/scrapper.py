import sys
import re
import os
import requests
from bs4 import BeautifulSoup

""" A web scrapper class that encapsulates neccessary methods and scripts to scrap a website
    Author - Medi W. Assumani

Methods:
    - download_data - Downloads the data from the given URL
    - clean_up_data - Cleans up a web page
    - write_in_file - Writes the cleaned up data into an internal text file
"""

class Scrapper(object):

    def __init__(self, url):
        """ The initializer that only takes in the website's url"""
        self.url = url
        self.raw_data = None
        self.clean_data = None
        self._download_data(url)
        self.clean_up_data()


    def _download_data(self, url):
        """ Downloads the data from the given URL
            @param - url: the url of the website to be scrapped
        """
        request = requests.get(url)
        status_code = request.status_code
        self.raw_data = request.text

        return self.raw_data

    def _clean_up_data(self):
        """ Cleans up a web page of HTML tags and unwanted characters
            @param - data: the data that has been scrapped
        """
        soup = BeautifulSoup(self.raw_data, "html.parser")
        self.clean_data = soup.find("div", "scrolling-script-container").text.strip()

    def write_in_file(self, file_name):
        """ Writes the cleaned up data into an internal text file"""

        with open(file_name, 'w') as file:
            file.write(clean_data)
