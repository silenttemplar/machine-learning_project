from sklearn import model_selection, svm, metrics
from sklearn.ensemble import RandomForestClassifier

def load_csv(fname):
    labels = []
    images = []

    with open(fname, 'r') as f:
        for line in f:
            cols = line.split(',')
            if len(cols) < 2: continue

            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)

    return {'labels':labels,'images':images}

def main():
    data = load_csv('./train.csv')
    test = load_csv('./t10k.csv')

    # print(type(data), type(test))

    clf = svm.SVC()
    # clf = RandomForestClassifier()
    clf.fit(data['images'], data['labels'])

    predict = clf.predict(test['images'])

    ac_score = metrics.accuracy_score(test['labels'], predict)
    cl_report = metrics.classification_report(test['labels'], predict)
    print('정답률=', ac_score)
    print('리포트=')
    print(cl_report)

if __name__ == "__main__":
    main()
