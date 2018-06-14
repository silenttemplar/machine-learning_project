import urllib.request as req

def main():
    local = "mushroom.csv"
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data'
    req.urlretrieve(url, local)
    print('ok')

if __name__ == "__main__":
    main()