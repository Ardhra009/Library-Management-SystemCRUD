from mysql import connector
class Library_connect:
    def get_connected(self):
        try:
            self.connection=connector.connect(
               host="localhost",
               user="root",
               password="Ardhra@17",
               database="library_db"
            )
            return self.connection
        except Exception as e:
            return None
class LibraryManager(Library_connect):
    def get(self):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query="select * from book"
            self.cursor.execute(query)
            record=self.cursor.fetchall()
            print(record)
        except Exception as e:
            print(e)
    def get_object(self,id=None):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query="select * from book where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            return None
    def retrieve(self,id=None):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query="select * from book where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            print(record)
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query="insert into book(book_name,author,category,price,quantity,publisher) values(%s,%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("book added successfully")
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
               self.connect=super().get_connected()
               self.cursor=self.connect.cursor()
               placeholder=""
               for k in kwargs.keys():
                   placeholder +=k + "=%s, "
               placeholder=placeholder.rstrip(", ")
               query=f"update book SET {placeholder} where id=%s"
               values=[v for v in kwargs.values()]
               values.append(id)
               self.cursor.execute(query,values)
               self.connect.commit()
               print("book updated successfully")
            else:
                print("book not found")
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query="select * from book where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            if record!=None:
                query="delete from book where id=%s"
                self.cursor.execute(query,values)
                self.connect.commit()
                print("book deleted successfully....!")
            else:
                print("book not found")
        except Exception as e:
            print(e)
obj=LibraryManager()
obj.get()
# obj.post(book_name="Python Basics",author="Meera",category="Programming",price=500.5,quantity=8,publisher="ABC")
# obj.post(book_name="SQL Basics",author="Meera",category="Programming",price=500.5,quantity=8,publisher="ABC")
# obj.post(book_name="Java",author="Meera",category="Programming",price=500.5,quantity=8,publisher="ABC")
obj.retrieve(id=2)
# obj.put(id=2,price=800.5)
# obj.delete(id=1)
