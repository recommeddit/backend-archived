#!/usr/bin/python

import sys
import recommendations


def main():
    # assume first argument is query. Default query is 'C++ IDE'
    try:
        query = sys.argv[1]
    except IndexError:
        query = "C++ IDE"

    results = recommendations.get_recommendations(query)

    print(results)


if __name__ == "__main__":
    main()
