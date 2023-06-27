"""
list = ['a', 'b', 'c']
"""
range(1, 5)  # ==> 1 2 3 4
range(3, 6)  # ==> 3 4 5

for x in range(1, 5):
    print(x)

# for x in MyRangeClass(1, 5):
#    print(x)

# for x in MyRangeClass(3, 6):
#    print(x)


class MyRangeClass:

    def __init__(self, start, end):
        self.value = start
        self.end = end
        # Facem clasa sa fie Iteratie

    def __iter__(self):

        return self

    def __next__(self):
        # conditia in care aruncam exceptia StorIteration

        if self.value >= self.end:

            raise StopIteration

        current_value = self.value
        self.value += 1
        return current_value


nums = MyRangeClass(1, 10)
for num in nums:
    print(num)

for number in MyRangeClass(1, 4):
    print(number)


# Generatorul Yield:


def my_gen():
    n = 1
    print('This is printed first')

    # Generator function contains yield statements
    yield n

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print('This is printed at last')
    yield n


for number in my_gen():
    print(number)

# my_gen()
# next(my_gen())
# n = next(my_gen())
# n = next(my_gen())
# print(n)
generator = my_gen()
print(next(generator))
print(next(generator))
print(next(generator))


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


# for number in MyRangeClass(1, 4):
#    print(number)

for number in my_range(1, 4):
    print(number)
