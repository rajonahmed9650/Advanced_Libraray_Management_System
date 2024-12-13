
import  json
def save_book(all_books):
    with open("data.json" , "w") as json_file:
        json.dump(all_books,json_file,indent=4)




def load_data():
    with open("data.json","r") as json_file:
        data = json.load(json_file)
        return  data


def lend_info(all_lend_info):
    with open("lend.json" , "w") as file:
        json.dump(all_lend_info,file,indent=4)


def lend_load_data():
    with open("lend.json","r") as file:
        lends = json.load(file)
        return lends

