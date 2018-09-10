import json


if __name__ == '__main__':

    # Deserialize s(a str)  to a Python object '
    json_format = json.loads('{"__complex__": true, "real": 1, "image": 2}')
    # traverse dict
    for x in json_format:
        print(x, json_format[x])
    print('comlex number is: ', json.loads(
        '{"__complex__": true, "real": 1, "image": 2}'))

    json_data = {'name': 'angle', 'age': 30, 'sex': 'F',
                 'favorite': 'food, travel, climb',
                 'books': [{'bookName': 'bigDad1'}, {'bookName': 'bigDad2'}]}

    # Serialize obj to a JSON formatted str "
    print('json dumps:', json.dumps(json_data))
    # pretty printing
    print('json dumps:', json.dumps(json_data, indent=4))

    # =====================

    json_data_1 = dict(name='angle', age=30, sex='F',
                  favorite='food, travel, climb',
                  books=[dict(name='bigDad1', desc='dad1desc'), dict(name='bigDad2', desc='dad2desc')])
    json_data_2 = dict(name=1, age=30, sex='F')

    print('json data 1: ', json.dumps(json_data_1, indent=4))

    # ======================
    json_data_3 = {}
    json_data_3['name'] = 'angle'
    json_data_3['age'] = 30
    json_data_3['favorite'] = 'food, travel, climb'
    json_data_3['books'] = []
    tmp = {}
    tmp['name'] = 'bigDad1'
    tmp['desc'] = 'dad1desc'
    json_data_3['books'].append(tmp)
    tmp['name'] = 'bigDad2'
    tmp['desc'] = 'dab2desc'
    json_data_3['books'].append(tmp)

    print('json data 3: ', json.dumps(json_data_3, indent=4))

