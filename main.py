#!/usr/bin/env python

import sys
import ast
from sorted_join import sorted_join


def main():
    assert(len(sys.argv) > 2), "Specify at least two lists"
    args = sys.argv[1:]
    arg_lists = []
    for arg_raw in args:
        arg_eval = ast.literal_eval(arg_raw)
        assert(isinstance(arg_eval, list)), "Each parameter must be a list"
        arg_lists.append(arg_eval)
    print(sorted_join(arg_lists))


if __name__ == "__main__":
    main()
