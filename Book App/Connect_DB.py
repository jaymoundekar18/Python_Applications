# Import required libraries
import pandas as pd
import sqlite3


class DB_Connect():
  
  # Setting up the database connection
  def __init__(self):
    self.conn = sqlite3.connect("book_users.db")
    self.cursor = self.conn.cursor()

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS user_data (
                          fullname TEXT NOT NULL,
                          email TEXT NOT NULL,
                          username TEXT NOT NULL,
                          password TEXT NOT NULL
                          )''')

# Database Operations
  
  def create_user(self, fname, mail, uname, passwd):
    self.cursor.execute("INSERT INTO user_data (fullname, email, username, password) VALUES (?,?,?,?) ",(fname,mail,uname,passwd))
    print("DB : User created")

## Book recored table for user
    table_name = fname.strip().replace(" ","").lower()
    query = "CREATE TABLE IF NOT EXISTS " + table_name + " (book_name TEXT NOT NULL, book_author TEXT NOT NULL, genre TEXT NOT NULL, reading_time TEXT, book_pages INTEGER NOT NULL, book_review TEXT, rating REAL)"
    
    self.cursor.execute(query)

    print("DB : Table created ", table_name)

    self.conn.commit()

## Display Particular user book data
  def show_book_data(self, tablename):
    query = "SELECT * FROM " + tablename
    self.cursor.execute("")
    result = self.cursor.fetchall()
    return result
  
## Display all Users in the Database
  def show_users_data(self):
    self.cursor.execute("SELECT * FROM user_data")
    result = self.cursor.fetchall()
    return result

## Find User
  def findUser(self,user,passwd):
        
        self.cursor.execute("SELECT * FROM user_data WHERE username=? AND password=?", (user, passwd))
        result = self.cursor.fetchone()
        print("DB : ",result)
        return result
  
## Find User Book Data
  def findUserBook(self,tablename):
        query = "SELECT book_name FROM " + tablename
        try:
           self.cursor.execute(query)
           result = self.cursor.fetchall()
           print("DB : ",result)
           return result
        
        except Exception as e:
           print(e)


## Adding New Book to the Particular Users Table
  def save_new_book(self, tablename, bookname, bookauthor,genre,bpages):
    query = "INSERT INTO " + tablename + "(book_name, book_author, genre, book_pages) values (?,?,?,?)"

    try:
      self.cursor.execute(query, (bookname, bookauthor, genre, bpages))
      print("DB : new book added")

      query = "SELECT * FROM " + tablename
      self.cursor.execute(query)
      self.conn.commit()
      res = self.cursor.fetchall()
      print(res)

    except Exception as e:
      print(e)


## Update Book Time
  def update_book_time(self,tablename, bookname, newtime):
    query = "UPDATE " + tablename + " SET reading_time = ? WHERE book_name = ?"
    try : 
      self.cursor.execute(query, (newtime,bookname ))
      self.conn.commit()
      print("DB : time updated")

      query = "SELECT * FROM " + tablename
      self.cursor.execute(query)
      res = self.cursor.fetchall()
      print(res)
    
    except Exception as e:
      print(e)


## Delete Table From Database
  def delete_table(self, tablename):
    query = "DROP TABLE IF EXISTS " + tablename.strip().replace(" ","").lower()
    try:
      self.cursor.execute(query)
      print(f"DB : {tablename} table deleted successfully")
      
    except Exception as e:
      print(e)
  



    
