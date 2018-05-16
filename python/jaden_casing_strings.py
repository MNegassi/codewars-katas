#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-

def toJadenCase(string):
    "capitalize each word in a sentence"
    return " ".join(substring.capitalize() for substring in string.split())


if __name__ == "__main__":
    print(toJadenCase("how can mirrors"))

