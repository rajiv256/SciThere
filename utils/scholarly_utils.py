import pandas as pd
import random
from utils import utils
from globals import SEARCH, DEFAULT_PUB
from scholarly import scholarly


def scholarly_journaldict2csv(data, csvfile=''):
    """The scholarly journal dict is of form
        <int>: {
            'name': <name>
            ...
        },...
    """
    df = pd.DataFrame(data=data)
    df = df.T # This is requried to modify the structure
    try:
        df.to_csv(csvfile)
    except:
        logging.info(f"{csvfile}: file doesn't exist! Error!")
    return

def select_random_journal(csvfile="data/journals.csv"):
    """If the same journal got selected in consecutive days, blame the 
    pseudo random number generator"""
    df = utils.read_csv2df(csvfile)
    names = list(df['name'])
    index = random.randint(0, len(names))
    return names[index]



def is_article(pub=None):
    if pub is None:
        return False
    if 'bib' not in pub:
        print("No bib")
        return False
    if 'venue' not in pub['bib'] or len(pub['bib']['venue']) < 5:
        print("venue issue")
        return False
    if 'num_citations' not in pub or pub['num_citations'] < 100:
        print("citations issue")
        return False
    if 'eprint_url' not in pub or (not utils.is_valid_url(pub['eprint_url'])):
        print("eprint issue")
        return False
    if 'pdf' not in pub['eprint_url']:
        return False
    return True

def dare_i_select(journalscsv="data/journals.csv"):

    journal = select_random_journal(journalscsv)
    search_query = scholarly.search_pubs('journal')
    skip = random.randint(SEARCH['START_FROM'], SEARCH['MAX_SKIP'])
    for i in range(skip):
        next(search_query)
    for i in range(SEARCH['EXPLORE_MAX']):  # see globals.py
        pub = next(search_query)
        if is_article(pub):
            return pub
    return DEFAULT_PUB
