from models.baseModel import BaseModel
import requests
from config import config


class Label(BaseModel):

    def __init__(self, project):
        self.type = 'labels'
        BaseModel.__init__(self, project, self.type)

    def delete(self, obj):
        request = requests.delete(self.url,
                                  data=obj,
                                  headers=config.headers)
        print(self.url)
        return request.status_code
