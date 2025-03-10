from sklearn import svm, metrics
import glob, os.path, re, json

def check_freq(fname):
    name = os.path.basename(fname)
    # print("name=", name)

    lang = re.match(r'^[a-z]{2,}', name).group()
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.lower()

    cnt = [0 for n in range(0, 26)]
    code_a = ord('a')
    code_z = ord('z')

    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z:
            cnt[n-code_a] += 1

    total = sum(cnt)
    freq = list(map(lambda n: n / total, cnt))
    return (freq, lang)

def load_files(path):
    # print(path)

    freqs = []
    labels = []
    file_list = glob.glob(path)
    for fname in file_list:
        # print("fname=", fname)

        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])

    return {'freqs':freqs, 'lables':labels}

def main():
    # for file in glob.glob('./*'):
    #     print(file)

    data = load_files('./train/*.txt')
    test = load_files('./test/*.txt')

    with open('./freq.json', 'w', encoding='utf-8') as fp:
        json.dump([data, test], fp)

    clf = svm.SVC()
    clf.fit(data['freqs'], data['lables'])

    predict = clf.predict(test['freqs'])

    ac_score = metrics.accuracy_score(test['lables'], predict)
    cl_report = metrics.classification_report(test['lables'], predict)
    print('정답률=', ac_score)
    print('리포트=')
    print(cl_report)

if __name__ == "__main__":
    main()