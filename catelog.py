#!/usr/bin/python3
from get_template import get_template
from cgi import FieldStorage

fields = FieldStorage()

print("Content-type: text/html\n")

print(get_template("temp.html").render(category = fields["category"]))
