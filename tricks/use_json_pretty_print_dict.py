my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}

print(my_mapping)
# {'b': 42, 'c': 12648430. 'a': 23}  ╮(╯﹏╰）╭


import json

print(json.dumps(my_mapping, indent=4, sort_keys=True))
# {
#     "a": 23,
#     "b": 42,
#     "c": 12648430
# }
# (￣▽￣)~*