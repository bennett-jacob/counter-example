import sys

from text_load import load
from text_prepoc import prepoc
from text_counter import counter
from proutput import output


def main():
    xo = load()
    prepoc_result = prepoc(xo)
    wc = counter(prepoc_result)
    output(xo, wc)


if __name__ == "__main__":
    sys.exit(main())
