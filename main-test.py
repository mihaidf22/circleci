#Import the Add function, and check if it works correctly
from main import Add

def TestAdd():
    assert Add(2,3) == 5
    print("Add function works correctly")

if __name__ == '__main__':
    TestAdd()