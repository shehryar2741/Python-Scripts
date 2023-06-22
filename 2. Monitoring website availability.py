"""

Implement a program using Python that monitors web sites and reports their availability.
This tool is intended as a monitoring tool for web site administrators for detecting problems on their sites.

Main functions:
1: Reads a list of web pages (HTTP URLs) from a configuration file.
2: Periodically makes an HTTP request to each page.
3: Measures the time it took for the web server to complete the whole request.
4: Verifies that the page content received from the server matches the content requirements
   (e.g., certain string in the web page).
5: Writes a log file that shows the progress of the periodic checks.

"""

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import configparser
import logging


def read_file(file_name):
    """
    :param file_name: this parameter gets the file from main function for reading
    :return: this function returns details_dict, head_dict items as the details
             dictionary contains https addresses and head dictionary contains titles
             of those webpages
    """

    config = configparser.RawConfigParser()
    config.read('Config file.TXT')

    details_dict = dict(config.items('SECTION_DETAILS'))
    head_dict = dict(config.items('SECTION_HEAD'))

    return details_dict, head_dict


def http_requests(details_dict, head_dict):
    """
    :param details_dict: gets the details of https addresses
    :param head_dict: gets the title of webpages
    """

    time = 0

    # This part logs the events in event.log file

    log = "event.log"
    logging.basicConfig(filename=log, level=logging.DEBUG,
                        format='%(asctime)s %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S')

    for item in details_dict:

        # This part sends http requests

        value = details_dict[item]

        r = urllib.request.urlopen(value)

        # This part counts the time taken for responses

        time1 = requests.get(value).elapsed.total_seconds()
        time += time1
        reqs = requests.get(value)

        # using the BeautifulSoup module for html parsing
        soup = BeautifulSoup(reqs.text, 'html.parser')

        # verifying and displaying the title
        title = soup.find('title')
        web_title = title.get_text()

        if web_title == head_dict[item]:
            print(f"Verified Title of the website is :", web_title)

    print(f"Total time taken for responses: ", time)

    logging.info("Total time takes is as follows:")
    logging.info(time)


def main():
    # The name of the file containing list of web pages
    Config_file = "Config file.TXT"

    # Calling the read_file function and getting the results of two dictionaries
    # from return through same function
    result1, result2 = read_file(Config_file)

    # Calling the http_requests function which uses result1 and result2
    # values which we got from read_file
    http_requests(result1, result2)


if __name__ == "__main__":
    main()