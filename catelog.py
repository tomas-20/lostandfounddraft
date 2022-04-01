from get_template import get_template

print("Content-type: text/html\n")

print(get_template("temp.html").render())
