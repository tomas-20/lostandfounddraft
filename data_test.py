from data_functions import *

if __name__ == "__main__":
    reset_data()
    add_item("outwear", "1/15/2020", "a nice blue jacket", "www.jackets.com/jackets?color=blue", b"azuuuuullll")
    add_item("outwear", "1/16/2020", "a nicer green jacket", "www.jackets.com/jackets?color=green", b"verrrrdeeeee")
    add_item("outwear", "1/16/2020", "a mediocre orange jacket", "www.jackets.com/jackets?color=orange", b"narannnjaaaa")
    print(get_next_id())
    update_found(1, True)
    print(get_items("outwear"))
