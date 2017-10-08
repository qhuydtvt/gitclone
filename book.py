from flask import Flask, render_template, request, redirect
import mlab
from mongoengine import *
mlab.connect()

app = Flask(__name__)

class Food(Document):
    name = StringField();
    description = StringField();
    image = StringField();



@app.route('/')
def index():
    return render_template('book.html',books=Food.objects())

@app.route('/admin')
def admin():
    return render_template('admin2.html', books=Food.objects())


@app.route('/ChooseBook/<book_id>')
def ChooseBook(book_id):
    bk= Food.objects().with_id(book_id)
    return render_template('test.html',book=bk)


@app.route('/delete_book/<book_id>')
def delete_book_id(book_id):
    book1= Food.objects().with_id(book_id)
    if book1 is not None:
        book1.delete()
        return redirect('admin')

if __name__ == '__main__':
  app.run(debug=True)
