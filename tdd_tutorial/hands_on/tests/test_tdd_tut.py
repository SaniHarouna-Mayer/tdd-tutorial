import pytest
from pathlib import Path
import ruamel.yaml as yaml
from tdd_tut import is_current
# @pytest.fixture()
# def itemdic():
#     return

cur_path = Path(__file__)
db_path = cur_path / ".."
print(cur_path, db_path)

@pytest.fixture()
def load_db():
    with open('../currenty_things.yml', 'r') as db:
        mydby = yaml.safe_load(db)
    return mydby

def test_is_current(load_db):
    for dic in load_db['sbillinge']['activities']:
        assert isinstance(is_current(dic), bool)
    for dic in load_db['sbillinge']['appointments'].values():
        assert isinstance(is_current(dic), bool)