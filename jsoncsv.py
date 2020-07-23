import json
import pandas as pd
import csv

myjsonfile=open(r'C:\Users\acer\Desktop\deneme.json')
jsondata=myjsonfile.read()
data=json.loads(jsondata)
y=pd.DataFrame(data,index=[0])
y.to_csv(r'C:\Users\acer\Desktop\test.csv')


myjson=open(r'C:\Users\acer\Desktop\deneme2.json')
jsondata2=myjson.read()
data2=json.loads(jsondata2)
y2=pd.DataFrame(data2,index=[0])
y2.to_csv(r'C:\Users\acer\Desktop\test2.csv')

reader1=csv.reader(open(r'C:\Users\acer\Desktop\test.csv'))
reader2=csv.reader(open(r'C:\Users\acer\Desktop\test2.csv'))

f=open("combined.csv","w")
writer=csv.writer(f)

for row in reader1:
    writer.writerow(row)
for row in reader2:
    writer.writerow(row)
f.close()
