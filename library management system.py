class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def disp_book(self):
        print(f"The available books in our library {self.name} are")
        for book in self.bookslist:
            print(book)


    def lend_book(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addbook(self, book):
        self.bookslist.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__== '__main__':
    library = Library(["Python", "Java", "C++", "Javascript", "React"], "Sujata")

    while (True):
        print(f"Welcome to the {library.name} library")
        print("Press\n"
              "1. To display the books\n"
              "2. To lend a book\n"
              "3. To add a book\n"
              "4. To return a book")
        user_choice1 = (input("Enter Your Choice:"))
        if user_choice1 not in ['1', '2', '3', '4']:
            print("PLease enter a valid option")
            continue
        else:
            user_choice1 = int(user_choice1)

        if user_choice1 ==1:
                library.disp_book()

        if user_choice1 == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name:")
            library.lend_book(user, book)
        elif user_choice1 == 3:
            book = input("Enter the name of the book you want to add:")
            library.addbook(book)
        elif user_choice1 == 4:
            book = input("Enter the name of the book you want to return:")
            library.returnBook(book)
        #else:
         #   print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2= ""
        while(user_choice2)!= "c" and user_choice2!="q":
            user_choice2 = input()

            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
            else:
                print("Not a valid option")








