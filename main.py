def gen_perms_v1(seq):
  """Generates all permutations of the given sequence. Each permutation is a
  list of the elements in SEQ in a different order. The permutations may be
  yielded in any order.

  >>> perms = gen_perms([100])
  >>> type(perms)
  <class 'generator'>
  >>> next(perms)
  [100]
  >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
  ...     next(perms)
  ... except StopIteration:
  ...     print('No more permutations!')
  No more permutations!
  >>> sorted(gen_perms([1, 2, 3])) # Returns a sorted list containing elements of the generator
  [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
  >>> sorted(gen_perms((10, 20, 30)))
  [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
  >>> sorted(gen_perms("ab"))
  [['a', 'b'], ['b', 'a']]
  """
  seq_num = len(seq)
  # input may not list
  seq = list(seq)
  if seq_num == 1:
      #base case
      yield seq
  else:
    gener_wo_first = gen_perms_v1(seq[1:])
    for permutation in gener_wo_first:
        for i in range(seq_num):
            permutation.insert(i, seq[0])
            yield permutation
            del permutation[i]

def gen_perms_v2(seq):
  """Generates all permutations of the given sequence. Each permutation is a
  list of the elements in SEQ in a different order. The permutations may be
  yielded in any order.

  >>> perms = gen_perms([100])
  >>> type(perms)
  <class 'generator'>
  >>> next(perms)
  [100]
  >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
  ...     next(perms)
  ... except StopIteration:
  ...     print('No more permutations!')
  No more permutations!
  >>> sorted(gen_perms([1, 2, 3])) # Returns a sorted list containing elements of the generator
  [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
  >>> sorted(gen_perms((10, 20, 30)))
  [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
  >>> sorted(gen_perms("ab"))
  [['a', 'b'], ['b', 'a']]
  """
  seq_num = len(seq)
  # input may not list
  seq = list(seq)
  if seq_num == 1:
      # base case
      yield seq
  else:
    gener_wo_first = gen_perms_v2(seq[1:])
    for permutation in gener_wo_first:
        for i in range(seq_num):
            yield permutation[:i] + seq[:1] + permutation[i:]

a = gen_perms_v1([1,2,3])
print('The v1 use for loop output:')
for i in a:
    print(i)

a = gen_perms_v1([1,2,3])
print('The v1 use sorted output:')
print(sorted(a))

b = gen_perms_v2([1,2,3])
print('The v2 use for loop output:')
for i in b:
   print(i)

b = gen_perms_v2([1,2,3])
print('The v2 use sorted output:')
print(sorted(b))
