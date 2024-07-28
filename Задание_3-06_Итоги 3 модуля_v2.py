data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def structure_sum(*args):
  sum = 0

  for object in args:

    if isinstance(object, str):
      sum += len(object)
    elif isinstance(object, int):
      sum += object
    elif isinstance(object, list):
      for element in object:
        sum += structure_sum(element)
    elif isinstance(object, tuple):
      for element in object:
        sum += structure_sum(element)
    elif isinstance(object, set):
      for element in object:
        sum += structure_sum(element)
    elif isinstance(object, dict):
      for key, value in object.items():
        sum += structure_sum(key, value)
  return sum

result = structure_sum(data_structure)
print(result)