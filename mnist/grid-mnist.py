import pandas as pd
from sklearn import model_selection, svm, metrics
from sklearn.model_selection import GridSearchCV

def main():
    train_csv = pd.read_csv('./train.csv')
    test_csv = pd.read_csv('./t10k.csv')

    train_label = train_csv.ix[:, 0]
    train_data = train_csv.ix[:, 1:785]
    test_label = test_csv.ix[:, 0]
    test_data = test_csv.ix[:, 1:785]

    params = [
        {"C":[1,10,100,1000], 'kernel':['linear']},
        {"C":[1,10,100,1000], 'kernel':['rbf'], 'gamma':[0.001, 0.0001]}
    ]


    clf = GridSearchCV(svm.SVC(), params, n_jobs=1)
    clf.fit(train_data, train_label)
    print('학습기=', clf.best_estimator_)

    pre = clf.predict(test_data)
    ac_sroce = metrics.accuracy_score(pre, test_label)
    print('정답률=', ac_sroce)

if __name__ == "__main__":
    main()