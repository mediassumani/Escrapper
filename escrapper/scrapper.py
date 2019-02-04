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

class Escrapper(object):

    def __init__(self, url):
        """ The initializer that only takes in the website's url"""
        self.url = url
        self._raw_data = None
        self._clean_data = None
        self.status_code = None
        self.is_data_written_in_file = False


    def download_data(self):
        """ Download the data from the given URL
            @param - url: the url of the website to be scrapped
        """
        request = requests.get(self.url)
        self.status_code = request.status_code
        self._raw_data = request.text

        return self._raw_data

    def clean_up_data(self):
        """ Clean up a web page of HTML tags and unwanted characters
            @param - data: the data that has been scrapped
        """
        soup = BeautifulSoup(self._raw_data, "html.parser")
        self._clean_data = soup.text

        return self._clean_data

    def write_in_file(self, file_name):
        """ Write the cleaned up data into an internal text file"""

        try:
            with open(file_name, 'w') as file:
                file.write(self._clean_data)

            self.is_data_written_in_file = True
        except IOError:
            raise("Error Found: Unable to open the text file.")
