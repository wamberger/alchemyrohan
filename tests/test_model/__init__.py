
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from tests.test_model.Parent import Parent
from tests.test_model.Child import Child