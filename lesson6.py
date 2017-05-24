#!/usr/bin/env python

def hello(name):
    print("Hello, " + name + " !")

def main():
    print("What is your name?")
    name = input()
    hello(name)

if __name__ == "__main__":
    main()