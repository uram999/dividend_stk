import requests as r
from bs4 import BeautifulSoup

import pandas as pd

row_html = r.get("https://www.dividend.com/dividend-stocks/10-year-dividend-increasing-stocks/#tm=3-10-years-increase-stocks&r=Webpage%231327&f_13=true&only=meta%2Cdata%2Cthead")
print(row_html)

soup = BeautifulSoup(row_html.content, 'html.parser')

table = soup.find('table')
div_df = pd.read_html(str(table))[0]
div_df.drop(["Unnamed: 0", "DARS™ Rating"], axis=1, inplace=True)
div_df.tail()