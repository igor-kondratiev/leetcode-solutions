"""Simple checker for basic solutions validation
"""


def check(solver, cases):
    """Performs simple solver check using test cases list
    The main logic is like:
        result = solver(*case.get('args', []), **case.get('kwargs', {})) == case['result']

    :param solver: task solver callable object
    :param cases: iterable object with test cases in dict format.
    Dict keys: args (optional), kwargs (optional), result (mandatory)
    """
    for i, case in enumerate(cases, 1):
        result = solver(*case.get('args', []), **case.get('kwargs', {})) == case['result']
        print "Test {0}: {1}".format(i, "OK" if result else "FAILED")
