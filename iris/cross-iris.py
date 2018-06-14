from sklearn import svm, metrics
import random, re

def getFile():
    with open('iris.csv', 'r', encoding='utf-8') as fp:
        lines = fp.read().split('\n')
        f_tonum = lambda n: float(n) if re.match(r'^[0-9\.]+$', n) else n
        f_cols = lambda li: list(map(f_tonum, li.strip().split(',')))
        return list(map(f_cols, lines))

def split_data_label(rows):
    data = []
    label = []
    for row in rows:
        data.append(row[0:4])
        label.append(row[4])
    return (data, label)

def calc_score(test, train):
    test_f, test_l = split_data_label(test)
    train_f, train_l = split_data_label(train)

    clf = svm.SVC()
    clf.fit(train_f, train_l)

    pre = clf.predict(test_f)
    return metrics.accuracy_score(test_l, pre)

def main():
    csv = getFile()
    del csv[0]
    random.shuffle(csv)

    K = 5
    csvk = [[] for i in range(K)]
    for i in range(len(csv)):
        csvk[i % K].append(csv[i])

    score_list = []
    for testc in csvk:
        trainc = []
        for i in csvk:
            if i != testc: trainc += i
        sc = calc_score(testc, trainc)
        score_list.append(sc)

    print('각각의 정답률=', score_list)
    print('평균 정답률=', sum(score_list) / len(score_list))

if __name__ == "__main__":
    main()