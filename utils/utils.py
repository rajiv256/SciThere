import random
import re
import os
import sys
import logging
import pandas as pd
import validators  # To validate urls
import requests

logging.getLogger(__name__)


def read_lines(filepath=None):
    if not os.path.exists(filepath):
        logging.info("File doesn't exist!")
        return 
    lines = []
    with open(filepath, 'r') as fin:
        lines = fin.readlines()
        lines = [line.strip() for line in lines]
    return lines 

def write_lines(lines, filepath=None):
    with open(filepath, 'w') as fout:
        for line in lines:
            fout.write(line + '\n')
    return

def read_csv2df(csvfile):
    df = pd.read_csv(csvfile)
    return df

def is_valid_url(url):
    return validators.url(url)

def download_pdf(url):
    response = requests.get(url)
    with open('currentpaper.pdf', 'wb') as f:
        f.write(response.content)
      