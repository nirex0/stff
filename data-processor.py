import os
import time

data_path = '/mnt/AI/darknet/data/drone/'
data_path = '/run/media/nirex/Local Disk/AI/darknet/data/drone/'
test_name_prefix = 'hyang'
valid_name_prefix = 'nexus'

train_files = []
test_files = []
valid_files = []

def generate_train():
    global train_files
    global test_files
    global valid_files
    
    all_files = os.listdir(data_path)
    all_txt = []
    for file in all_files:
        file = str(file.strip())
        if file.endswith('.txt'):
            # f = open(data_path + file, 'r')
            # content = f.read()
            # if content == "":
            #     continue
            
            if file.startswith(test_name_prefix):
                test_files.append(file.replace('.txt', '.jpg'))
            elif file.startswith(valid_name_prefix):
                valid_files.append(file.replace('.txt', '.jpg'))
            else:
                train_files.append(file.replace('.txt', '.jpg'))      
        else:
            continue
    train_files.sort()
    test_files.sort()
    valid_files.sort()   

def write_list_to_file(lst: list, fname: str):
    f = open(fname, 'w')
    for item in lst:
        f.write('data/drone/' + str(item).strip() + '\n')
    f.close()

if __name__ == '__main__':
    print("Generating New Annotation Data...")
    generate_train()

    print(train_files[0])
    print(test_files[0])
    print(valid_files[0])

    print("Saving Test...")
    write_list_to_file(test_files, './drone-test.txt')

    print("Saving Valid...")
    write_list_to_file(valid_files, './drone-valid.txt')

    print("Saving Train...")
    write_list_to_file(train_files, './drone-train.txt')
    
