import unittest
import os
from models.base_model import BaseModel
from storage.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.obj = BaseModel()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_new(self):
        self.storage.new(self.obj)
        self.assertIn(self.obj.id, self.storage.all())

    def test_save(self):
        self.storage.new(self.obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        self.storage.new(self.obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn(self.obj.id, self.storage.all())

if __name__ == '__main__':
    unittest.main()
