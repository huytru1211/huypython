class Publication:
    def __init__(self,name):
        self.name = name

    def print_information(self):
        print(f"Publication: {self.name}")

class Book(Publication):
    def __init__(self,name, author, page):
        super().__init__(name)
        self.author = author
        self.page = page

    def print_information(self):
        print("Book")
        super().print_information()
        print(f"Author name: {self.author}")
        print(f"Page: {self.page}")

class Magazine(Publication):
    def __init__(self,name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print("Magazine")
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")

book = Book("Compartment No.6", "Rosa Liksom", "192")
magazine = Magazine("Donal Duck", "Aki Hyyppa")
book.print_information()
"\n"
magazine.print_information()
