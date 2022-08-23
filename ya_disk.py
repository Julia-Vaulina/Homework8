from pprint import pprint

import requests

token = 

class YaDisk:
    def __init__(self, token):
        self.token = token

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/last-uploaded'
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {self.token}'}
        response = requests.get(files_url, headers=headers)
        return response.json()

    def get_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {self.token}'}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self.get_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        return response.status_code

    def new_folder_disk(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {self.token}'}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.put(upload_url, headers=headers, params=params)
        return response.json()

    def del_folder_disk(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {self.token}'}
        params = {"path": disk_file_path, "permanently": "true"}
        response = requests.delete(upload_url, headers=headers, params=params)
        if response.status_code == 204:
            print("Success")
        return response.status_code


if __name__ == '__main__':
    disk = YaDisk(token=token)
    pprint(disk.upload_file_to_disk("Netology/Foto.jpg", "Калининград.jpg"))