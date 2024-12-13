import Add_book
import Save_all_book
import Lend_book
import Return_book



all_books = Save_all_book.load_data()
while True:
    print("Welcome Advanced Library Management System")
    print("0.Exit")
    print("1.Add book")
    print("2.Lend book")
    print("3.Return book")

    choice = input("Enter your choice:")
    if choice == "0":
        print("Thanks using for Advanced Library Management System ")
        break
    elif choice == "1":
        Add_book.add_book(all_books)
    elif choice == "2":
        Lend_book.lend_book()
    elif choice == "3":
        Return_book.return_book()

    else:
        print("Invalid choice")