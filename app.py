from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, cover_url FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

@app.route('/')
def index():
    books = get_books()
    return render_template('index.html', books=books)

@app.route('/borrow/<int:book_id>')
def borrow(book_id):
    # For now we just show a message - you can enhance this
    return f"<h1>Book with ID {book_id} has been marked as borrowed.</h1><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
