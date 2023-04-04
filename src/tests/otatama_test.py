import unittest
from entities.otatama_task import Task
from repositories.otatama_repository import OtatamaRepository



class TestOtatama(unittest.TestCase):
    def setUp(self):
        OtatamaRepository.delete()
        self.task = Task()

    
        

