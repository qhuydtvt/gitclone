from flask import Flask, render_template, request


app = Flask(__name__)

books=[
{
"name": "Sách học tập",
"image": "http://product.hstatic.net/1000068419/product/upload_f4c72179b92d4c8892088eef6539bd86.jpg"
},

{"name":"Sách giải trí",
"image":"https://i.ytimg.com/vi/dAJxweLeOZg/maxresdefault.jpg"
},

{"name":"Sách Bán Chạy",
"image":"https://thiepmung.com/images/frame/frame_demo/bikip-0-1-demo57b1a8af66423.jpg"
}
]

@app.route('/')
def index():
    return render_template('book.html',books=books)

if __name__ == '__main__':
  app.run(debug=True)
