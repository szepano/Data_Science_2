import pandas as pd

tmp = pd.read_html("https://en.wikipedia.org/wiki/Demographics_of_Ukraine")


if __name__ == '__main__':
    print(tmp)