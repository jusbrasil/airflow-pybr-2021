import sys

import pandas


def movie_choose(type):
    df = pandas.read_csv("fixtures/movies.csv")
    filter_by_movie_type = df["Genre"] == type
    return ",".join(
        df[filter_by_movie_type].sample().astype(str).values.flatten().tolist()
    )


if __name__ == "__main__":
    type = sys.argv[1]
    sys.stdout.write(movie_choose(type))
