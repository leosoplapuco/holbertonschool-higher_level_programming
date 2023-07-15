#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1
argv = sys.argv[1:]

print(argc, "argument" + ("s" if argc != 1 else "") + ":")
if argc == 0:
    print("No arguments.")
else:
    for i, arg in enumerate(argv, 1):
        print(i, ":", arg)
