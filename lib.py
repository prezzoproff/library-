
# Coding a library system that will store books, users and check out user checkout and returning of books
# a class to handle the books
class Books():
    def __init__(self):
        self.book_title = []
#function of handling book search
    def search_book (self, bookdetails):
        if bookdetails in self.book_title:
            
            print(f"{bookdetails} is available in the library")
        else:
            print(f"{bookdetails} is not available in the library")
# adding books to the system
    def addbook (self, book_title):
        if book_title not in self.book_title:
            self.book_title.append(book_title)
            print(f"{book_title} has been successfully added")
        else:
            print(f"{book_title} already exists in the system")
 # class to handle users       
class Users():
    def __init__(self):
        self.users = {}
#searching users
    def searchUser(self, user_details):
        if user_details in self.users:
            print(f"Name: {user_details.title()}, Address : {self.users[user_details]}")
        else:
            print(f"{user_details} not available in the system")
            
#adding users
    def adduser (self, user_name, user_email):
        if user_name not in self.users:
            self.users[user_name] = user_email
            print(f"{user_name} has been added to the system")
        else:
            print(f"{user_name} already exists")
#library to handle both classes
class Library(Books, Users,):
    def __init__(self):
        Books.__init__(self)
        Users.__init__(self)
        self.issuedbooks = []
#checking out books
    def checkoutbook(self, book_details):
        if book_details in self.book_title:
            self.book_title.remove(book_details)
            self.issuedbooks.append(book_details)
            print(f"{book_details} has been checked out")
        else:
            self.book_title.append(book_details)
            print(f"{book_details} wasnt updated in the system but it has been")
            print(f"{book_details} has been checked out")
#returning books
    def bookcheckin(self, book_details):
        if book_details in self.issuedbooks:
            self.issuedbooks.remove(book_details)
            self.book_title.append(book_details)
            print(f"{book_details} has been checked in")
        else:
            self.book_title.append(book_details)
            print(f"{book_details} wasnt updated in the system but it has been")
            print(f"{book_details} has been added in the system")
        


lib = Library()
lib.addbook("atomic habits")
lib.adduser("fortunata", "fortunata@gmail")
lib.search_book("death")
lib.search_book("atomic habits")
lib.searchUser("john")
lib.checkoutbook("goodlife")
lib.bookcheckin("python")
lib.addbook("Moments")
lib.checkoutbook("Moments")
lib.search_book("Moments")
lib.bookcheckin("Moments")
lib.search_book("Moments")
lib.adduser("kasyoka", "kasyokas2@gmail.com")
lib.searchUser("kasyoka")
