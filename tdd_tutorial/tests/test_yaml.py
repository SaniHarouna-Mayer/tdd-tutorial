import pytest
import yaml
from tdd_tutorial.tdd_tut import is_current



@pytest.fixture()
def load_db():
    with open('../currenty_things.yml', 'r') as db:
        mydby = yaml.full_load(db)
    return mydby

def test_is_current(mydby):
    for dic in mydby['sbillinge']['activities']:
        assert isinstance(is_current(dic), bool)
    for dic in mydby['sbillinge']['appointments'].values():
        assert isinstance(is_current(dic), bool)

