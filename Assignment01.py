#Library Management System
import random

#add books
def add_book(book_list):
    chk = "yes"
    while(chk == "yes"):
        book_id = input("Enter id of book: ")
        title = input("Enter title of book: ")
        author_name = input("Enter author name of book: ")
        publish_year = input("Enter publish year of book: ")
        books = {"book_id": book_id,"title": title,"author_name": author_name,"publish_year": publish_year,"status": True}
        book_list.append(books)
        print("book list=", book_list)
        chk = input("do you want to add more books? (yes or no): ")
    return book_list

#find book
def find_book(book_list, book_id):
    for books in book_list:
        if books["book_id"] == book_id:
            return books
    return None

#borrow book
def borrow_book(book_list):
    x = "yes"
    while(x == "yes"):
        book_id = input("enter id of book to borrow: ")
        books = find_book(book_list, book_id)
        if books is None:
            print("book not found")
        elif books["status"] == True:
            books["status"] = False
            print("book borrowed successfully!")
        else:
            print("book is already borrowed!")
        x = input("do you want to borrow another book? (yes or no): ")

#return book
def return_book(book_list):
    book_id = input("enter id of book to return: ")
    books = find_book(book_list, book_id)
    if books is None:
        print("book not found")
    elif books["status"] == True:
        print("this book was not borrowed")
    else:
        books["status"] = True
        print(f"'{books['title']}' (ID {books['book_id']}) has been returned successfully.")

#display all books
def display_all_books(book_list):
    if not book_list:
        print("No books in the library.")
    else:
        for books in book_list:
            print(f"ID: {books['book_id']}, Title: {books['title']}, Author: {books['author_name']}, Year: {books['publish_year']}, Status: {'Available' if books['status'] else 'Borrowed'}")

#get available books
def get_available_books(book_list):
    available = []
    for books in book_list:
        if books["status"] == True:
            available.append(books)
    return available

#save to file
def save_to_file(book_list, filename):
    with open(filename, "w") as file:
        for books in book_list:
            line = f"{books['book_id']},{books['title']},{books['author_name']},{books['publish_year']},{books['status']}"
            file.write(line + "\n")
    print("Books saved successfully.")

#load from file
def load_from_file(filename):
    book_list = []
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("file not found. starting with an empty inventory.")
        return book_list

    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        books = {"book_id": parts[0],"title": parts[1],"author_name": parts[2],"publish_year": parts[3],"status": parts[4] == "True"}
        book_list.append(books)
    file.close()
    return book_list

#make books
def make_books():
    titles = [("Maths", "Rowling", 2000),("English", "Ali Khan", 2015),("Computer", "Sara Ahmed", 2010)]
    book_list = []
    id_number = 1
    for title, author_name, year in titles:
        for copy in range(5):
            books = {"book_id": str(id_number),"title": title,"author_name": author_name,"publish_year": str(year),"status": random.choice([True, False])}
            book_list.append(books)
            id_number += 1
    return book_list

#menu
def show_menu(books):
    running = True
    while running:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Find Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Show Available Books")
        print("7. Save to File")
        print("8. Load from File")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")
        if choice == "1":
            add_book(books)
        elif choice == "2":
            book_id = input("enter id of book to find: ")
            result = find_book(books, book_id)
            print(result)
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            display_all_books(books)
        elif choice == "6":
            print(get_available_books(books))
        elif choice == "7":
            save_to_file(books, "library.txt")
        elif choice == "8":
            books = load_from_file("library.txt")
        elif choice == "9":
            print("Goodbye!")
            running = False
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

#Print
if __name__ == "__main__":
    books = make_books()
    show_menu(books)