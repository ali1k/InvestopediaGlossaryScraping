import os, json

file1 = open('../FULL_URL_INDEX.txt', 'r')
Lines = file1.readlines()
list = []
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    list.append(line.strip())
    #print(line.strip())


path_to_json = '../data/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
for link in json_files: 
    with open('../data/'+link) as f:
        data = json.load(f)
        #print (data['@id'])
        if data['@id'] in list:
            list.remove(data['@id'] )
print(list) # print items which are not scraped

