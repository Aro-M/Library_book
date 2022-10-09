import  json
import  sqlite3

class  Library:
    def  __init__(self):
        self.lib_book = {}

    def  add_book(self,book_name,book_rating):
        if book_name  is not  self.lib_book.keys():
           self.lib_book[book_name] = book_rating
        else:
            print(f"{book_name} Book already  in the  Library with Book ratings {self.lib_book.get(book_name)}")

    def  change_book_name(self,book_name,new_book_name,book_rating):
        if  book_name not in self.lib_book.keys():
            print(f"\n {book_name} Book does not exist  in the  Library ")
        else:
             self.lib_book.pop(book_name)
             self.lib_book[new_book_name] = book_rating


    def  change_book_rating(self,book_name,new_rating):
        if  book_name not in self.lib_book.keys():
            print(f"\n {book_name} Book does not exist in the Library")
        else:
            self.lib_book[book_name] = new_rating
            print(f"\n{book_name} Book   rating  updated to {new_rating}"  )

    def  get_all_book(self):
          for  i in self.lib_book:
            print(f"\n {i} , {self.lib_book[i]}")

    def delete_book(self,book_name):
        if book_name not in self.lib_book.keys():
            print(f"\n{book_name} Book  does not exist in the Library ")
        else:
            self.lib_book.pop(book_name)
            print(f"\n {book_name} Book has been deleted  form the Library ")

    def get_book_by_name(self,book_name):
        if book_name not in self.lib_book.keys():
            print(f"\n {book_name} Book does not exist in the Library.")
        else:
            book = self.lib_book.get(book_name)
            print(f"\n Here is the ,", book)

    def get_book_by_rating(self,book_rating):
        books = self.lib_book.values()
        book_same_rating = {}
        for book in books:
            if book_rating in book.values():
                book_same_rating.update(book)
        print("\n Non Book has the rating of %s" %{book_rating} if  book_same_rating  == {} else print(book_same_rating))

    def  set_data_json_file(self):
        json_lib_write = json.dumps(self.lib_book,indent=4)
        with open("library.txt",'w') as outLib:
            outLib.write(json_lib_write)

    def get_data_json_file(self):
        with open("library.txt" ,'r') as inLib_read:
            json_lib_read = json.load(inLib_read)
        for i in json_lib_read:
            print(f"{i} ,{json_lib_read[i]} \n")
    # def  open_data_sqlite(self):
    #
    #     # base = sqlite3.connect("new_lib.db")
    #     # cur = base.cursor()
    #     # query = "insert into table_name " + str(tuple(self.lib_book.keys())) + " values" + str(tuple(self.lib_book.values())) + ";"
    #     # base.execute(query)
    #     # base.commit()
    #     # base.close()





library = Library()

library.add_book(book_name="Charls Petcold" ,book_rating=7)

library.add_book(book_name="Mark Lutz" ,book_rating=3)

library.add_book(book_name="Effetive Meyers" ,book_rating=10)

library.add_book(book_name="100 days  of coding" ,book_rating=4)

library.add_book(book_name="Python cookbook" ,book_rating=2)

library.add_book(book_name="Steven Prata" ,book_rating=6)

# library.get_all_book()

library.add_book(book_name="Fluent Python clear" ,book_rating=8)

library.change_book_rating(book_name="Python cookbook",new_rating=14)

library.change_book_rating(book_name="Mark Lutz",new_rating=8)

# library.get_all_book()

library.get_book_by_name("Mark Lutz")

# library.delete_book("Mark Lutz")

library.change_book_name(book_name="Fluent Python clear" ,new_book_name="flu clear",book_rating=8)

library.get_all_book()

library.change_book_name(book_name="Mark Lutz" ,new_book_name="fl clear",book_rating=8)

library.set_data_json_file()
library.get_data_json_file()
# library.open_data_sqlite()


