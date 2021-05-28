#!/usr/bin/python

import recommendations


def search(request):
    if request.args and 'query' in request.args:
        query = request.args.get('query')
    else:
        query = ""
    results = recommendations.get_recommendations(query)

    return results, 200, {'Access-Control-Allow-Origin': '*'}


def main():
    # assume first argument is query. Default query is 'C++ IDE'
    try:
        import sys
        query = sys.argv[1]
    except IndexError:
        query = "similar movies to inception"

    results = recommendations.get_recommendations(query)

    print(results)


if __name__ == "__main__":
    main()
