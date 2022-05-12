from sqlite3 import connect, Row
from os import system

def reset_data():
    open("data.db", "w").close()
    db = connect("data.db")
    c = db.cursor()
    c.execute("CREATE TABLE mesa (id INTEGER, found INTEGER, image_count INTEGER, category TEXT, date TEXT, description TEXT, link TEXT)")
    db.commit()
    db.close()
    system("rm www/lostitem*")

def get_next_id():
    db = connect("data.db")
    c = db.cursor()
    c.execute("SELECT MAX(id) FROM mesa")
    max_id = c.fetchone()[0]
    db.close()
    if max_id == None:
        return 0
    return max_id + 1

def id_to_filenames(id, image_count):
    filenames = []
    base_filename = f"www/lostitem{str(id)}"
    suffix_number = ord("a")
    for i in range(image_count):
        filenames.append(base_filename + chr(suffix_number))
        suffix_number += 1
    return filenames

def add_images(id, images):
    filenames = id_to_filenames(id, len(images))
    print("filenames are: " + str(filenames))
    for image, filename in zip(images, filenames):
        with open(filename, "wb") as file:
            file.write(image)

def add_item(category, date, description, link, images):
    id = get_next_id()
    db = connect("data.db")
    c = db.cursor()
    c.execute("INSERT INTO mesa VALUES (?, 0, ?, ?, ?, ?, ?)", (id, len(images), category, date, description, link))
    db.commit()
    db.close()
    add_images(id, images)

def row_to_dic(row):
    dic = dict(row)
    dic.pop("found")
    dic.pop("category")
    dic["filenames"] = id_to_filenames(dic["id"], dic["image_count"])
    dic.pop("id")
    return dic

def get_items(category):
    db = connect("data.db")
    c = db.cursor()
    c.row_factory = Row
    c.execute("SELECT * FROM mesa WHERE category = ? AND found = 0", (category,))
    result = list(map(row_to_dic, c.fetchall()))
    db.close()
    return result

def update_found(id, found):
    db = connect("data.db")
    c = db.cursor()
    c.execute("UPDATE mesa SET found = ? WHERE id = ?", (int(found), id))
    db.commit()
    db.close()
