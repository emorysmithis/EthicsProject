# Functions 
def test(x): 
    print("This is a test function")
    return "{} was passed from main".format(x)


# Main Execution 
if __name__ == '__main__': 
    print("This is the main function of game.py") 
    x = 10
    test(x)

