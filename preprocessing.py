filename = "data.csv"
fw = open("traindata.txt", "w+")
fwtest = open("testdata.txt", "w+")
cnt = len(open(filename, "r").readlines())
fr = open(filename, "r")
line = fr.readline()
traincnt = cnt * 0.9
t = 1
while 1:        #divide the data into to testdata and traindata
    line = fr.readline()
    if t <= traincnt:
        t += 1
        items = line.split(";")
        for i in range(11):
            if i == 1 or i == 2 or i == 4 or i == 7 or i == 8 or i == 9:
                a = float(items[i]) * 10
                if i == 4:
                    a *= 10
                fw.write(str(a) + " ")
                continue
            if i == 5:
                a = float(items[i]) / float(items[i + 1]) * 5
                fw.write(str(a) + " ")
                continue
            if i == 6:
                continue
            fw.write(items[i] + " ")
        fw.write(items[11])
    elif t > traincnt and t < cnt:
        t += 1
        items = line.split(";")
        for i in range(11):
            if i == 1 or i == 2 or i == 4 or i == 7 or i == 8 or i == 9:
                a = float(items[i]) * 10
                if i == 4:
                    a *= 10
                fwtest.write(str(a) + " ")
                continue
            if i == 5:
                a = float(items[i]) / float(items[i + 1]) * 5
                fwtest.write(str(a) + " ")
                continue
            if i == 6:
                continue
            fwtest.write(items[i] + " ")
        fwtest.write(items[11])
    else :
        break

fr.close()
fw.close()
fwtest.close()
