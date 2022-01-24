nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


def flat_generator(nested_list):
    values = nested_list
    for value in values:
        for item in value:
            yield item
     

for item in  flat_generator(nested_list):
	print(item)