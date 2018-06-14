import matplotlib.pyplot as plt
import pandas as pd
import json

def main():
    with open('./freq.json', 'r', encoding='utf-8') as fp:
        freq = json.load(fp)

    lang_dic = {}
    for i, lbl in enumerate(freq[0]['lables']):
        fq = freq[0]['freqs'][i]
        if not (lbl in lang_dic):
            lang_dic[lbl] = fq
            continue
        for idx, v in enumerate(fq):
            lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v) / 2

    asclist = [[chr(n) for n in range(97, 97+26)]]
    df = pd.DataFrame(lang_dic, index=asclist)

    plt.style.use('ggplot')
    df.plot(kind='bar', subplots=True, ylim=(0,0.15))
    plt.savefig('lang-plot.png')

if __name__ == '__main__':
    main()