import struct

def to_csv(name, maxdata):
    lbl_f = open('./'+name+"-labels-idx1-ubyte", 'rb')
    img_f = open('./'+name+"-images-idx3-ubyte", 'rb')
    csv_f = open('./'+name+'.csv', 'w', encoding='utf-8')

    mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
    mag, img_coung = struct.unpack(">II", img_f.read(8))
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixels = rows * cols

    res = []
    for idx in range(lbl_count):
        if idx > maxdata: break
        label = struct.unpack('B', lbl_f.read(1))[0]
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label)+",")
        csv_f.write(','.join(sdata)+"\r\n")
        if idx < 10:
            s = "P2 28 28 255\n"
            s = s + " ".join(sdata)
            iname = "./{0}-{1}-{2}.pgm".format(name, idx, label)
            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)
    csv_f.close()
    lbl_f.close()
    img_f.close()

if __name__ == "__main__":
    to_csv("train", 100)
    to_csv("t10k", 500)