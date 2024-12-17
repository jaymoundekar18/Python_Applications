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
    self.cursor.execute("INSERT INTO user_data (fullname, email, username, password) VALUES (?,?,?,?) ",(name,mail,uname,passwd))

## Book recored table for user
    table_name = fname.strip().replace(" ","").lower()
    query = "CREATE TABLE IF NOT EXISTS " + table_name + " (book_name TEXT NOT NULL, book_author TEXT NOT NULL, genre TEXT NOT NULL, reading_time TEXT, book_pages INTEGER NOT NULL, book_review TEXT, rating REAL)"
    self.cursor.execute(query)

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

  def delete_record(self):
    pass

  def update_record(self):
    pass

  def delete_table(self, tablename):
    query = "DROP TABLE IF EXISTS " + tablename.strip().replace(" ","").lower()
    try:
      self.cursor.execute(query)
      print(f"{tablename} table deleted successfully")
      
    except Exception as e:
      print(e)
      
  
    



    
