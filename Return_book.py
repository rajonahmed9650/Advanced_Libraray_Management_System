
import Save_all_book

def return_book():
    title = input("Enter book title to return: ")
    lends = Save_all_book.lend_load_data()
    books = Save_all_book.load_data()
    for lend in lends:
        if lend['title'] == title:
            lends.remove(lend)


            for book in books:
                if book['title'] == title:
                    if 'quantity' not in book:
                        book['quantity'] = 0
                    book['quantity'] += 1
            print(f"Book '{title}' has been returned successfully.")
            break
    else:
        print(f"No such book '{title}' found in lend records.")


    Save_all_book.lend_info(lends)
    Save_all_book.save_book(books)





