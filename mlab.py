import mongoengine



host = "ds113935.mlab.com"
port = 13935
db_name = "book"
user_name = "tipro1810"
password = "645hoanghoatham"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
