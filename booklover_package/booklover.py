import pandas as pd

class BookLover:
    '''This class stores the personal and book information of a reader'''
    def __init__(self, name, email, fav_genre, num_books = None, book_list = None):
        self.name = name 
        self.email = email 
        self.fav_genre = fav_genre
        self.num_books = 0 if num_books is None else num_books
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]}) if book_list is None else book_list
        
    
    def add_book(self, book_name, book_rating):
        if book_name not in list(self.book_list.book_name):
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
                })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else: 
            print(book_name + ' is already in the book list')
            
    def has_read(self, book_name):
        return(book_name in list(self.book_list.book_name))
    
    def num_books_read(self):
        return(len(self.book_list))
    
    def fav_books(self):
        return(self.book_list.loc[self.book_list['book_rating']>3])
    