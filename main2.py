from fastapi import FastAPI
from schemas import Book
import sqlite3

app = FastAPI()

@app.get('/')
def home():
    return {'key': 'Hello )'}

@app.post('/Book')
def create_Book(item:Book):
    insert_testdata(item)
    return item



def insert_testdata(records):
    print(records)

    try:
        sqlite = sqlite3.connect('server2.db')
        cursor = sqlite.cursor()

        cursor.executemany("INSERT INTO prices VALUES(?,?,'Алматы')", records)
        sqlite.commit()
        print("Запись успешно добавлена ")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if sqlite:
            sqlite.close()
            print("Соединение с базой данных закрыто")

