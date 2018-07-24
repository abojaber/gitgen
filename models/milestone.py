from models.baseModel import BaseModel


class Milestone(BaseModel):

    def __init__(self, project):
        self.type = 'milestones'
        BaseModel.__init__(self, project, self.type)
