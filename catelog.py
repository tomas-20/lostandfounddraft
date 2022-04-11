#!/usr/bin/python3
from get_template import get_template
from data_functions import get_items
from cgi import FieldStorage

category_names = {"outerwear": "Outerwear", "gloveshatsscarves": "Gloves, Hats, and Scarves", "personalschoolsupplies": "Personal School Supplies", "bookspapers": "Books, Textbooks, and Papers", "smallitems": "Small Items"}

fields = FieldStorage()

print("Content-type: text/html\n")

category = fields.getvalue("category")

print(get_template("temp.html").render(category = category, category_name = category_names[category], items = get_items(category)))
