import os


class Human(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print ('Hello World ' + self.name)


damian = Human('Damian')
damian.hello()

print (__name__)

if __name__ == "__main__":
    print ("Hello Main")
    pass