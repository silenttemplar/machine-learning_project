import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

def main():
    mr = pd.read_csv('mushroom.csv', header=None)

    label = []
    data = []
    attr_list = []

    for row_index, row in mr.iterrows():
        label.append(row.ix[0])
        row_data = []
        for v in row.ix[1:]:
            row_data.append(ord(v))
        data.append(row_data)

    data_train, data_test, label_train, label_test = train_test_split(data, label)

    clf = RandomForestClassifier()
    # clf = svm.SVC()
    clf.fit(data_train, label_train)

    predict = clf.predict(data_test)

    ac_score = metrics.accuracy_score(label_test, predict)
    cl_repost = metrics.classification_report(label_test, predict)

    print('정답률=', ac_score)
    print('리포트=')
    print(cl_repost)

if __name__ == '__main__':
    main()