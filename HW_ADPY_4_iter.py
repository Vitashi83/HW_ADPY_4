class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list
        
    def __iter__(self):
        self.main_list_cursor = 0  # курсор основного списка
        self.nested_list_cursor = -1 # курсор списка вложенного в основной список
        return self

    def __next__(self):
        self.nested_list_cursor += 1    # увеличиваем nested_list_cursor
        if self.nested_list_cursor == len(self.main_list[self.main_list_cursor]): # если во вложенном списке элементы закончились,
            self.main_list_cursor +=1  # то переходи на следующий список увеличив main_list_cursor
            self.nested_list_cursor = 0 # и обнуляем main_list_cursor
        if self.main_list_cursor == len(self.main_list):
            raise StopIteration
        return self.main_list[self.main_list_cursor][self.nested_list_cursor]


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
