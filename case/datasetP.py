import dataset
import sqlite3

"""
with dataset.connect('sqlite:///../data/my_database.db') as db:
    db['some_table'].insert(dict(name='John Doe', age=37))
    db['some_table'].insert(dict(name='Jane Doe', age=34, gender='female'))
"""
with dataset.connect('sqlite:///../data/my_database.db') as db:
    john = db['some_table'].find_one(name='John Doe')
    print('john', john)
    print(db.tables)
    print(db['some_table'].columns)
    print(len(db['some_table']))
    db['some_table'].all()