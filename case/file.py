import json


if __name__ == '__main__':
    # construct json data, dict type
    json_data = {'name': 'angle', 'age': 30, 'sex': 'F',
                 'favorite': 'food, travel, climb',
                 'books': [{'name': 'bigDad1'}, {'name': 'bigDad2'}]}

    # create new file
    with open('../data/data.json', 'w') as f:
        # write data in file
        json.dump(json_data, f, indent=4)

    # open file
    with open('../data/data.json') as f:
        # read file data
        json_data = f.read()
        print(json_data)


