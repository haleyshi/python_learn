import re

output = ''' Id    Name                           State
----------------------------------------------------
 2     instance-00000003              running
 3     instance-00000004              running'''


tuples = output.split('\n')

if tuples is not None:
    if len(tuples) >= 2:
        del tuples[0]
        del tuples[0]

        for tuple in tuples:
            tuple = tuple.strip()
            tuple = re.sub(r'\s+', ' ', tuple)
            fields = tuple.split(' ')
            print fields


