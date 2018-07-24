from models.label import Label
from models.milestone import Milestone
from models.issue import Issue
from templates import simple
import sys


project_id = sys.argv[1]

lbl_result = {}
mls_result = {}

for label in simple.labels:
    lbl_result[label['name']] = Label(project_id).create(label)

for milestone in simple.milestones:
    mls_result[milestone['title']] = Milestone(project_id).create(milestone)
    for task in simple.issues[milestone['title']]:
        print(mls_result[milestone['title']])
        task['milestone_id'] = mls_result[milestone['title']]['id']
        print(Issue(project_id).create(task))
