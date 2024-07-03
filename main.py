from mod_scraping import *
from mod_excel import *
import os

pega_reviews()
exporta_reviews()
os.startfile("polished_reviews.xlsx")
