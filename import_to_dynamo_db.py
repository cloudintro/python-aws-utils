import json

def write_to_file(file_data, name):
    target_file_name = f'class_test_result_{name}.json'
    print(f'Writing to {target_file_name}')
    with open(target_file_name, 'w') as target_file:
        file_data_new = {'key' : f'CLASS_TEST_{name}', 'data' : file_data}
        target_file.write(json.dumps(file_data_new))
        target_file.close()

def read_from_file():
    source_file_name = 'class_test_result_all.json'
    print('Reading from {source_file_name}')
    with open(source_file_name, 'r+') as source_file:
        file_data = json.load(source_file)
        print(file_data)
        count = 1
        for data in file_data.get('data'):
            write_to_file(data, data['name'])
            count+=1
        print(f'Total {count} result created')
        source_file.close()

if __name__ == '__main__':
    read_from_file()