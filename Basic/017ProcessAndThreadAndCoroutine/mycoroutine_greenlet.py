

from greenlet import greenlet

def sing():
    print('sing')
    print('i"ve finished song')
    # g2.switch()

def dance():
    print('dancing')
    print('i"ve finished dancing')
    # g1.switch()


if __name__ == "__main__":
    g1 = greenlet(sing)
    g2 = greenlet(dance)

    g1.switch()
    g2.switch()







