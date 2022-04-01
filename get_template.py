from jinja2 import Template

def get_template(filename):
    with open(filename, "r") as file:
        return Template(file.read())
