import simple_math

# tot_sum = n(n+1)/2
# n=10 => tot_sum = 55

def test_simple_math():
    assert simple_math.simple_math(10) == 55

"""
I made a mistake:
collected 1 item                                                                                                                               

test_simple_math.py F                                                                                                                    [100%]

=================================================================== FAILURES ===================================================================
_______________________________________________________________ test_simple_math _______________________________________________________________

    def test_simple_math():
>       assert simple_math(10) == 55
               ^^^^^^^^^^^^^^^
E       TypeError: 'module' object is not callable. Did you mean: 'simple_math.simple_math(...)'?

test_simple_math.py:7: TypeError
=========================================================== short test summary info ============================================================
FAILED test_simple_math.py::test_simple_math - TypeError: 'module' object is not callable. Did you mean: 'simple_math.simple_math(...)'?
============================================================== 1 failed in 0.15s ===============================================================

Corrected it and then it worked:
============================================================= test session starts ==============================================================
platform linux -- Python 3.12.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/Karlsson/Doktorandkurser/AdvancedPythonProgramming/Day4
collected 1 item                                                                                                                               

test_simple_math.py .                                                                                                                    [100%]

============================================================== 1 passed in 0.21s ===============================================================
"""