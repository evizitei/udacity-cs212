# In the first "Andy's Corner" series in the course,
# Andy asserts that a for loop (compared to list comprehensions)
# is BAD, UGLY, and SLOW.  I have to yield on the first 2 points,
# but I suspect that behind the scenes a list comprehension is 
# basically doing a for loop, I can't think of a reason why
# it should be slower.  Let's find out:

def test_for_loop():
  input_data = ["stan", "kyle", "cartman", "kenny", "randy", "santa"]
  uppered_data = []
  for i in range(len(input_data)):
    uppered_data.append(input_data[i].upper())

def test_comprehension():
  input_data = ["stan", "kyle", "cartman", "kenny", "randy", "santa"]
  uppered_data = [i.upper() for i in input_data]


if __name__ == '__main__':
  import timeit
  print(timeit.timeit("test_for_loop()", number=10000, setup="from __main__ import test_for_loop"))
  print(timeit.timeit("test_comprehension()", number=10000, setup="from __main__ import test_comprehension"))


"""
evizitei-laptop:udacity-cs212 evizitei$ python list_comprehensions.py
0.215728998184
0.145558834076
evizitei-laptop:udacity-cs212 evizitei$ vim list_comprehensions.py
evizitei-laptop:udacity-cs212 evizitei$ python list_comprehensions.py
2.16237092018
1.41216206551
evizitei-laptop:udacity-cs212 evizitei$ vim list_comprehensions.py
evizitei-laptop:udacity-cs212 evizitei$ python list_comprehensions.py
22.5341989994
15.0162990093


Indeed, with several different values of 'number', list compreshensions are
faster.

After doing some reading (https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
I determined this is due to comprehensions pushing the looping structure
itself down into compiled C code rather than running each low level
statement in the iteration up in the interpreter.
"""
