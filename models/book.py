from mongoengine import Document, StringField
from faker import Faker

class Food(Document):
    name = StringField();
    description = StringField();
    image = StringField();
# food = Food(name = "vkl",image = "https://sachcuabanblog.files.wordpress.com/2015/11/kimcuongbdt_m1.jpg?w=474",description="VKLASLDASDA");
#
# food.save()
def dumb_data():

    f=Faker()
    for i in range(3):
        book= Food(name=f.name())
    book.save()
