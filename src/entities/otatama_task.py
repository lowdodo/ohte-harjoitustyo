
#will be used later on MAYBEEBEBEBEBBE
#from time import datetime 

from random import *

# this is what a one task does
class Task:

    def __init__(self, task, state=False, user=None, task_id=None ):
        self.task = task
        self.state = state #if not done, false
        self.user = user
        self.id = task_id


