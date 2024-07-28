from django.test import TestCase
from django.conf import settings
from decouple import Config, RepositoryEnv

from pymongo import MongoClient
import os


base_dir = os.getcwd()
ENV = Config(RepositoryEnv(base_dir + '/.env'))

# Create your tests here.
class TestDatabase(TestCase):
    def test_db_query(self):
        dbClient = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = dbClient[settings.DATABASES['default']['NAME']]
        COLLECTION_NAME = 'django_migrations'
        result = db[COLLECTION_NAME].find_one()
        print(result)
