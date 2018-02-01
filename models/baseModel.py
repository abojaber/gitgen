import requests
from config import config


class BaseModel:

    def __init__(self, project, obj):
        self.obj = obj
        self.url = config.api['base_url'] + '/api/v4/projects/{}/{}'.format(project, self.obj)

    def create(self, obj):
        request = requests.post(self.url,
                                data=obj,
                                headers=config.headers)
        return request.json()

    def delete(self, obj):
        request = requests.delete(self.url + '/{}'.format(obj),
                                  # data=obj,
                                  headers=config.headers)

        return request.status_code
