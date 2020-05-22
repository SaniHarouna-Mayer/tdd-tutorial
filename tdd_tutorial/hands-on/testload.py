import yaml

with open('currenty_things.yml', 'r') as db:
    mydby = yaml.full_load(db)

for key, val in mydby['sbillinge']:
    print(key)
    print(val)
print(mydby['sbillinge'])

