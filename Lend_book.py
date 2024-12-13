from datetime import datetime,timedelta
import  Save_all_book

def lend_book():
    books = Save_all_book.load_data()
    title = input("Enter book title:")

    for book in books:
        if book["title"] == title and book["quantity"] >0:
            name = input("Enter your name:")
            try:
                phone = input("Enter your phone:")
            except ValueError:
                print("Invalid Phone number:")
            due_date = datetime.now() + timedelta(days=10)

            all_lend_info = Save_all_book.lend_load_data()
            lend_info = {
                "name" : name,
                "phone" : phone,
                "title" : title,
                "due_date" : due_date.strftime("%Y-%m-%d")
            }

            all_lend_info.append(lend_info)
            Save_all_book.lend_info(all_lend_info)

            book["quantity"] -=1
            Save_all_book.save_book(books)
            print(f"Books {title} has been lent.Return date {due_date}")
            return
    print("Sorry , The book is not available")

