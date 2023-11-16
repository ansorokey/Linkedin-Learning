import itertools

# the cycle method iterates in a loop endlessly
seq1 = ['Dante', 'Vergil', 'Nero']
iter1 = itertools.cycle(seq1)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

# the count creates a counter with a starting and step value
count1 = itertools.count()
print(next(count1))
print(next(count1))
print(next(count1))

# the accumulate aggregates values together,
# defaults to addition but the function can be changed
vls = [10, 20, 30, 40, 50, 60, 70, 80, 90]
acc = itertools.accumulate(vls, max)
print(next(acc))
print(next(acc))
print(next(acc))


# the chain connects sequences together
abcs = 'abc'
one_two_threes = '123'
chain = itertools.chain(abcs, one_two_threes)
print(list(chain))


# dropwhile and takewhile will return values until a condition is met
# takewhile will return values until it fails a condition
# dropwhile will ignore values until it passes a test
# passing or failing a test after doesnt matter
vls = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def bigger_than_40(x):
    return x < 40

take = list(itertools.takewhile(bigger_than_40, vls))
print(take)
drop = list(itertools.dropwhile(bigger_than_40, vls))
print(drop)
