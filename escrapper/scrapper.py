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
        self.data = None


    def _download_data(url):
        """ Downloads the data from the given URL
            @param - url: the url of the website to be scrapped
        """
        request = requests.get(url)
        status_code = request.status_code
        data = request.text

        return data

    def clean_up_data(data):
        """ Cleans up a web page of HTML tags and unwanted characters
            @param - data: the data that has been scrapped
        """
        soup = BeautifulSoup(data, "html.parser")
        cleaned_up_data = soup.find("div", "scrolling-script-container").text.strip()

        return cleaned_up_data

    def write_in_file(data, file_name):
        """ Writes the cleaned up data into an internal text file"""

        with open(file_name, 'w') as file:
            file.write(data)
