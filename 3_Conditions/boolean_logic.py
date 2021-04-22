
boolean_statements = [
    1 > 5,  # 1
    1 < 5,  # 2
    10 == 10,  # 3
    1 != 10,  # 4
    True and False,  # 5
    True and True,  # 6
    False and False,  # 7
    True or True,  # 8
    True or False,  # 9
    False or True,  # 10
    False or False,  # 11
    ]

for statement in enumerate(boolean_statements, 1):
    print(statement)
