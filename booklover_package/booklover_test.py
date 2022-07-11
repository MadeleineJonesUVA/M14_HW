from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase): 
    def test_1_add_book(self): #Add a book and test if it is in book_list.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        
        self.assertTrue("War of the Worlds" in list(test_object.book_list.book_name))
    
    def test_2_add_book(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds", 4)
        
        expected = 1
        self.assertEqual(len(test_object.book_list), expected) 
        
    def test_3_has_read(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        
        self.assertTrue(test_object.has_read('War of the Worlds'))
        
    def test_4_has_read(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        
        self.assertFalse(test_object.has_read('Harry Potter'))
        
    def test_5_num_books_read(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Harry Potter", 2)
        test_object.add_book("Gone with the Wind", 3)
        test_object.add_book("Educated", 5)
        
        expected = 4
        self.assertEqual(expected, test_object.num_books_read())
        
    def test_6_fav_books(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Harry Potter", 2)
        test_object.add_book("Gone with the Wind", 3)
        test_object.add_book("Educated", 5)
        
        favs = test_object.fav_books()
        self.assertTrue(all(i >3 for i in favs['book_rating']))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)