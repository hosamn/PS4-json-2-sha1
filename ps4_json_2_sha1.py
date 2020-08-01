import json
import os

# Change the working directory to the py file dir:
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Get a list of current dir json files:
for root, dirs, files in os.walk("."):
    # print(len(files), files)
    json_files = [f for f in files if f.endswith('.json')]
    break  # break after reporting current dir files and don't go deeper

# print(json_files)

for json_file in json_files:

    out_file_name = json_file.split('.')[0]+'.sha1'

    with open(json_file) as opf:
        data = json.loads(opf.read())

    for i in range(data['numberOfSplitFiles']):
        piece_name = data['pieces'][i]['url'].split('/')[-1]
        piece_hash = data['pieces'][i]['hashValue']
        file_line = piece_hash + ' *' + piece_name
        with open(out_file_name, 'a') as outt:
            outt.write(file_line+'\n')
