from firebase_admin import db

root = 'cases-data'


def load_data(*args):
    ref = db.reference().child(root)
    for x in args:
        ref = ref.child(x)
    data = ref.get()
    print('loaded-> ', data, '<-end of loading')
    return data


def save_data(data, *args):
    ref = db.reference().child(root)
    for x in args:
        ref = ref.child(x)
    ref.update(data)
    print('saved-> ', data, '<-end of saving')


def save_data_all(dictionary):
    db.reference().child(root).set(dictionary)
