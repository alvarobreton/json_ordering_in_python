from urllib.request import urlopen
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = urlopen(url)
data_json = json.loads(response.read())

result = []
check = 0
records = []
i = 0
y = 0
for data in data_json :
    if data['userId'] == check: 
        records_body = {'userId':data['userId'],'id' : data['id'],'title' : data['title'], 'body' : data['body']}
        records.insert(i, records_body)
        if(i == len(data_json) - 1): 
            result.insert(y, {y : {'records' : records}})
    else:
        if check != 0:
            result.insert(y, {y : {'records' : records}})
            records = []
            y = y + 1
        check = data['userId'];
        records_body = {'userId':data['userId'],'id' : data['id'],'title' : data['title'], 'body' : data['body']}
        records.insert(i, records_body)
        
    i = i + 1;
print (result)
