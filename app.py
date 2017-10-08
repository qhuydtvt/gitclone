from flask import Flask, render_template, request, redirect
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

@app.route('/admin')
def admin():
    return render_template('admin.html', girl_types=GirlType.objects())

@app.route('/delete_girl_type/<girl_id>')
def delete_girl_type(girl_id):
    girl_type= GirlType.objects().with_id(girl_id)
    if girl_type is not None:
        girl_type.delete()
        return redirect('admin')


# get girl type from mongoengine
# render found

# btvn 1: lam admin
# 2: edit girl type : optional

if __name__ == '__main__':
  app.run(debug=True)
