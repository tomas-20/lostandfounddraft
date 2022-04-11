from data_functions import *

if __name__ == "__main__":
    reset_data()
    add_item("outerwear", "1/15/2020", "a nice blue jacket", "https://www.jackets.com/jackets?color=blue", b"azuuuuullll")
    add_item("outerwear", "1/16/2020", "a nicer green jacket", "https://www.jackets.com/jackets?color=green", b"verrrrdeeeee")
    add_item("outerwear", "1/16/2020", "a mediocre orange jacket", "https://www.jackets.com/jackets?color=orange", b"narannnjaaaa")
    print(get_next_id())
    update_found(1, True)
    print(get_items("outerwear"))
