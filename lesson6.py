#!/usr/bin/env python

# "while" sentence

def hello(name):
    print("Hello, " + name + " !")

def main():
    print("What is your name?")
    name = input()
    if name == "Dima":
        hello(name)
    elif name == "Vova":
        print("Hey, Vova")
    else:
        print("By-by")

if __name__ == "__main__":
    main()