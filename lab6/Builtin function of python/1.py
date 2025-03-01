from functools import reduce
import operator

numbers = [2, 3, 4, 5]
result = reduce(operator.mul, numbers)
print(result)
