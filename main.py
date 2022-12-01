from pip._vendor import requests
import json

heroes_list = ['Hulk', 'Captain america', 'Thanos']
intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

for hero in heroes_list:
    hero_dict = json.loads(requests.get(url + hero).content)
    intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])



from pip._vendor import requests
import json
from pprint import pprint
HTTP_STATUS_CREATE: int = 201

class YandexDisk:
    URL_FILES_LIST: str = 'http://cloud-app.net/v1/disk/resources/files'
    URL_UPLOAD_LIST: str = 'http://cloud-app.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token
    def header(self):
        return {
            'Content-Type': 'application/json',
            'authorization': f'QAuth {self, token}'
        }
    
    def get_file_list(self):
        response = requests.get(self.URL_FILES_LIST, headers = self.header)
        return response.json()
    
    def get_upload_link(self, ya_disk_path: str):
        params = {'path': ya_disk_path, 'overwrite': 'true'}
        response = requests.get(self.URL_UPLOAD_LIST, headers = self.heade, params = params)
        upload_url = response.json().get('href')
        return upload_url

    def upload_file(self, ya_disk_path: str, file_path: str):
        upload_link = self.get_upload_link(ya_disk_path)
        with open (file_path, 'rd') as file_obj:
            response = requests.put(upload_link, data = file_obj)
            if response.satus_code == HTTP_STATUS_CREATE:
                print('Успешно загружен')
        return response.status_code

instansce = YandexDisk(token)
print(instansce.upload_file('3.txt', '3.txt')) 



from pip._vendor import requests
from datetime import timedelta
from datetime import datetime

def search_tag(days, tag):

    final_date = int(datetime.timestamp(datetime.now()))
    initial_date = final_date - days * 86400

    params = {
        'previous_day': initial_date,
        'the_next_day': final_date,
        'tagged': tag,
        'site': 'stackoverflow'
    }

    response = requests.get('https://api.stackexchange.com/2.2/questions', params=params)
    for question in response.json().get('items'):
        print ("Самые популярные запросы с  тэгом 'Python': " + str(question['tags']), '\n')

search_tag(2, 'python')
