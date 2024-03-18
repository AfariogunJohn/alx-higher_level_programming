#!/usr/bin/env python3

import doctest
import sys

def run_tests(test_file):
    """Run the doctests in the specified file."""
    results = doctest.testfile(test_file)
    if not results.failed:
        print("All tests passed!")
    else:
        print("Some tests failed. See above for details.")
    return results.failed

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test.py <test_file>")
        sys.exit(1)
    test_file = sys.argv[1]
    num_failed = run_tests(test_file)
    sys.exit(num_failed)

