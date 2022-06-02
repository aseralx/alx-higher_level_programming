#!/usr/bin/python3

if __name__ == "__main__":
    """print the name of argumnent and number"""
    import sys

    for i in range(0,len(sys.argv)):
        if i >= 1:
            print(f"{i}: {sys.argv[i]}")
        else:
            if len(sys.argv) > 2:
                print(f"{len(sys.argv) - 1} arguments:")
            elif len(sys.argv) - 1 == 1:
                print(f"{len(sys.argv) - 1} argument:")
            else:
                print(f"{len(sys.argv) - 1} arguments.")
