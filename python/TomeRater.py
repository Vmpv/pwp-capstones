class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The email of the user {}  has been updated to {}".format(self.name, self.email))

    def __repr__(self):
        return ("The user: {}, with email: {}, has {} books read".format(self.name, self.email, len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def get_average_rating(self):
        books_count = 0
        rtg_summ = 0
        for rtg in self.books.values():
            if rtg:
                books_count += 1
                rtg_summ += rtg
                avgrtg = rtg_summ / books_count
        return avgrtg

    def read_book(self, book, rating=None):
        self.books[book] = rating

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_ISBN):
        self.isbn = new_ISBN
        print("The ISBN of the book {} has been updated to {}".format(self.title, self.isbn))

    def add_rating(self, rating):
        if rating:
            if rating > 0 and rating < 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __repr__(self):
        return self.title

    def get_average_rating(self):
        rtg_summ = 0
        for rtg in self.ratings:
            rtg_summ += rtg
        if len(self.ratings) > 0:
            avg_rtg = rtg_summ / len(self.ratings)
        else:
            avg_rtg = 0
        return avg_rtg


class Fiction(Book):

    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return ("{} by {}".format(self.title, self.author))


class Non_Fiction(Book):

    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return ("{}, a {} manual on {}".format(self.title, self.level, self.subject))


class TomeRater(object):

    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "TomeRater {} and {}".format(self.users, self.books)

    def __str__(self):
        return "in TomeRater users are {} and books are {}".format(self.users, self.books)

    def __eq__(self, other_rater):
        if self.users == other_raters.users and self.books == other_rater.books:
            return True
        else:
            return False

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_nf = Non_Fiction(title, subject, level, isbn)
        return new_nf

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email " + email)

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for item in self.books:
            print(item)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        times_read = 0
        most_read = None
        for book in self.books:
            number_of_reads = self.books[book]
            if number_of_reads > times_read:
                times_read = number_of_reads
                most_read = book
        return most_read

    def highest_rated_book(self):
        highest_rating = 0
        most_rated_book = None
        for book in self.books:
            bookavgrtg = book.get_average_rating()
            if bookavgrtg > highest_rating:
                highest_rating = bookavgrtg
                most_rated_book = book
            return most_rated_book

    def most_positive_user(self):
        high_rating = 0
        positive_user = None
        for user in self.users.values():
            useravgrtg = user.get_average_rating()
            if useravgrtg > high_rating:
                high_rating = useravgrtg
                positive_user = user
        return positive_user
