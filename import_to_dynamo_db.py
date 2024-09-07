import json

_source_file_name = 'class_test_result_all.json'

def write_to_file(result_dict, result_type):
    count = 0
    for name, result in result_dict.items():
        target_file_name = f'{result_type}_result_{name}.json'
        print(f'Writing to {target_file_name}')
        with open(target_file_name, 'w') as target_file:
            file_data = {result_type : name, 'result' : result}
            target_file.write(json.dumps(file_data))
            target_file.close()
        count+=1
    print(f'Total {count} {result_type} result created')

def build_result_dict(result, result_dict, result_key):
    name = f'{result[result_key]}'
    if result_dict.get(name) is not None:
        result_dict[name] = result_dict[name] + [result]
    else:
        result_dict[name] = [result]

def read_from_file():
    print(f'Reading from {_source_file_name}')
    with open(_source_file_name, 'r+') as source_file:
        file_data = json.load(source_file)
        print(file_data)
        subject_result_dict = {}
        student_result_dict = {}
        count = 0
        for result in file_data.get('result'):
            build_result_dict(result, subject_result_dict, 'subject')
            build_result_dict(result, student_result_dict, 'name')
            count+=1
        source_file.close()
        print(f'Total {count} result found in {_source_file_name}')
    write_to_file(subject_result_dict, 'subject')
    write_to_file(student_result_dict, 'student')

if __name__ == '__main__':
    read_from_file()