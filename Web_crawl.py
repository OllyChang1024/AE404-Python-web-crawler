import requests

url = 'https://www.pagamo.org/map?course_code=hccc'

data = requests.get(url)
print(data)
print(data.text)



































