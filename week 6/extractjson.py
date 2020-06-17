import json
import urllib.request

input = input('Enter location:')
print('Retrieving', input)
#url = 'http://py4e-data.dr-chuck.net/comments_678629.xml'
data = urllib.request.urlopen(input).read()
print('Retrieved',len(data),'charachters')

info = json.loads(data)
#print(info)
#[print(item['count']) for item in info['comments']]
sum = sum([ int(item['count']) for item in info['comments']])
print('Count: ',len(info['comments']))
print('sum: ',sum)
