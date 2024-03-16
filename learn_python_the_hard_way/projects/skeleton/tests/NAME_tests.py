from nose.tools import *
import module_1
def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN")
    
setup()
teardown()
test_basic()

a = module_1.Init()
a.print()