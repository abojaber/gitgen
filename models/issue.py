from models.baseModel import BaseModel


class Issue(BaseModel):

    def __init__(self, project):
        self.type = 'issues'
        BaseModel.__init__(self, project, self.type)
