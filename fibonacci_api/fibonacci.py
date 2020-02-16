"""
A fibonacci sequence starting from first index and ending at end index generator.

Usage:
# >>> from fibonacci import Fibonacci
# >>> f = Fibonacci()
# >>> g = f.generate(1, 5)
# >>> next(g)
0
# >>> next(g)
1
# >>> f.sequence(1, 5)
[1, 1, 2, 3, 5]

"""

__all__ = ["Fibonacci"]

try:
    xrange
except NameError:
    xrange = range


def singleton(cls):
    """A singleton decorator for classes"""
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Fibonacci(object):

    def __init__(self):
        self.results = [0, 1, 2]

    def compute(self, num1, num2):
        for i in xrange(len(self.results), num2):
            self.results.append(self.results[i - 1] + self.results[i - 2])

    def generate(self, num1, num2):
        """Returns a python generator represents the numbers in
        the fibonacci sequence (starts from num1 to num2). Python generator is more
        memory efficient
        """
        self.compute(num1, num2)

        for i in xrange(num1, num2):
            yield self.results[i]

    def sequence(self, num1, num2):
        """Returns the numbers in the fibonacci sequence as a list"""
        self.compute(num1, num2)

        if num1 == 0:
            return self.results[num1:num2]
        else:
            return self.results[num1 - 1:num2]


if __name__ == '__main__':
    import sys
    import cProfile

    # Act as a command line tool and take a number from command line
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except:
        raise SystemExit("Please enter a positive integer")

    fib = Fibonacci()
    my_statement = 'seq = fib.sequence(num1, num2)'

    if sys.stdout.isatty():
        cProfile.run(my_statement)
    else:
        exec (my_statement)
        #print(fib_sequence)
