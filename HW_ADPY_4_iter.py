class FlatIterator:

    def __init__(self, nested_list):
        self.list = - 1
        self.end = len(nested_list)
       

    def __iter__(self):
        return self


    def __next__(self):
        self.list += 1
        if self.list == self.end:
            raise StopIteration
        return '\n'.join(str(item) for item in nested_list[self.list])

    
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
	    print(item)   
