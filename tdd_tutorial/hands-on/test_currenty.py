import pytest
import yaml
from tdd_tutorial.tdd_tut import is_current

# @pytest.fixture()
# def itemdic():
#     return

@pytest.fixture():
    with open('currenty_things.yml', 'r') as db:
        mydby = yaml.full_load(db)
    return mydby

print(mydby)

def test_is_current(itemdic):
    for dic in itemdic['sbillinge']['activities']:
        assert isinstance(is_current(dic), bool)
