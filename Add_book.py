
import Save_all_book

def add_book(all_books):
    title = input("Enter book title:")
    author = input("Enter book author:")
    try:
        quantity  = int(input("Enter book quantity:"))
    except ValueError:
        print("Invalid input:")


    new_book = {
        "title" : title,
        "author" : author,
        "quantity": quantity
    }

    all_books.append(new_book)
    Save_all_book.save_book(all_books)
    print("Book added Successfully")