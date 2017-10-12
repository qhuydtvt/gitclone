from flask import *
import mlab
from mongoengine import *
mlab.connect()
from models.book import Food, dumb_data

app = Flask(__name__)

class Food(Document):
    name = StringField();
    description = StringField();
    image = StringField();

class Number(Document):
    number = IntField();
# for i in range(0,100):
#     numbers= Number(number= i)
#     numbers.save()
@app.route('/a')
def index2():
    return render_template('test.html',books=Number.objects())


@app.route('/')
def index():
    return render_template('book.html',books=Food.objects())

@app.route('/admin')
def admin():
    return render_template('admin2.html', books=Food.objects())


@app.route('/ChooseBook/<book_id>')
def ChooseBook(book_id):
    bk= Food.objects().with_id(book_id)
    return render_template('book_detail.html',book=bk)



@app.route('/delete_book/<book_id>')
def delete_book_id(book_id):
    book1= Food.objects().with_id(book_id)
    if not book1:
        book1.delete()
        return redirect('admin')

@app.route('/book_edit/<book_id>')
def edit(book_id):
    bk= Food.objects().with_id(book_id)
    return render_template('edit.html',book=bk)

@app.route('/Switch')
def bmi():
    args = request.args
    book_detail = str(args["book_detail"])



    for boo in Food.objects():
        if boo.name == book_detail:
            return render_template("book_detail.html", book= boo)
        return "Sai Chỗ"




if __name__ == '__main__':
  app.run(debug=True)
