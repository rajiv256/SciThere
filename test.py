from scholarly import scholarly
from pprint import pprint 
import pandas as pd
from utils import utils, scholarly_utils 
from openai import OpenAI
from tqdm import tqdm
# client = OpenAI()


# d = scholarly.get_journals(category='English', subcategory=None, include_comments = False)
# To create the journals.csv file
# utils.scholarly_journaldict2csv(d, "data/journals.csv")

# df = utils.read_csv2df("data/journals.csv")
# print(utils.select_random_journal())

# search_query = scholarly.search_pubs('computer science')
# import validators


# queries = []
# for i in tqdm(range(5)):
#     queries.append(next(search_query))
#     b = scholarly_utils.is_article(queries[-1])
#     if b:
#         pprint(queries[-1])
#         print("===========================")

pub = scholarly_utils.dare_i_select()
pprint(pub)
utils.download_pdf(pub['eprint_url'])