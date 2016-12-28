import yaml

yamltxt = """
sgh:
    name:
        first: Guohuang
        last: Shi
    sex: Male
    info:
    - Tall
    - Rich
    - Handsome
"""

sgh = yaml.load(yamltxt)

print sgh

print yaml.dump(sgh)