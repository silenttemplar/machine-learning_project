import random

def calc_bmi(h, w):
    bmi = w / (h/100) ** 2
    if bmi < 18.5: return 'thin'
    if bmi < 25: return 'normal'
    return 'fat'

def main():
    cnt = {'thin':0, 'normal':0, 'fat':0}

    with open('bmi.csv', 'w', encoding='utf-8') as fp:
        fp.write('height,weight,label\r\n')

        for i in range(20000):
            h = random.randint(120,200)
            w = random.randint(35,80)
            label = calc_bmi(h,w)
            cnt[label] += 1
            fp.write("{0},{1},{2}\r\n".format(h,w,label))

    print('ok', cnt)

if __name__ == "__main__":
    main()
