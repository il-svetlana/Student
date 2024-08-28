first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) > 4]
print('first_result: ', first_result)
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print('second_result: ', second_result)
third_result = {x: len(x) for x in first_strings + second_strings if not len(x) % 2}
print('third_result: ', third_result)