from flask import Flask, render_template, request
import mlab
from mongoengine import *
app = Flask(__name__)

mlab.connect()

class GirlType(Document):
    name = StringField()
    image = StringField()
    description = StringField()


@app.route('/')
def index():
    return render_template('index.html', girl_types=GirlType.objects())


@app.route('/bmi-calc')
def bmi_calc():
    return render_template("bmi_calc.html")


@app.route('/bmi')
def bmi():
    args = request.args
    weight = int(args["weight"])
    height = int(args["height"]) / 100
    bmi = weight / (height ** 2)
    return str(bmi)


if __name__ == '__main__':
  app.run(debug=True)
