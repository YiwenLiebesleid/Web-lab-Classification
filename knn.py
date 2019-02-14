import numpy as np
import operator

def dist(line1, line2):
    dis = 0.0
    for i in range(10):
        dis += (line1[i] - line2[i]) ** 2
    dis //= 2
    return dis

def cosdist(line1, line2):
    dis = 0.0
    disdiv1 = 0.0
    disdiv2 = 0.0
    for i in range(10):
        dis += line1[i] * line2[i]
        disdiv1 += line1[i] ** 2
        disdiv2 += line2[i] ** 2
    disdiv1 //= 2
    disdiv2 //= 2
    dis = dis / (disdiv1 * disdiv2)
    return dis

def insert(topk, temp, k):
    for i in range(k):
        if(temp[1] < topk[i,1]):
            for j in range(k - 1, i, -1):
                topk[j] = topk[j - 1]
            topk[i] = temp
            break
        else :
            if (topk[i, 1] == -1):
                topk[i] = temp
                break
            continue

def getmost(topk, k):
    #times = np.array([[0,0],[0,0],[0,0],[0,0],[0,0]])
    times = []
    for i in range(k):
        times.append([0,0])
    times = np.array(times)
    for i in range(k):
        for j in range(k):
            if topk[i, 0] == times[j, 0]:
                times[j, 1] += 1
                break
            elif times[j, 0] == 0:
                times[j] = [topk[i, 0], 1]
                break
    max = 0
    maxi = 0
    for i in range(k):
        if max < times[i, 1]:
            max = times[i, 1]
            maxi = i
    return times[maxi, 0]


def classify(dataline, traindata, ntrain, k, way):
    #topk = np.array([[-1.0,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]])#k = 5
    topk = []
    for i in range(k):
        topk.append([-1.0,-1])
    topk = np.array(topk)
    dis = 0.0
    for i in range(ntrain):
        if way == 0:
            dis = dist(dataline, traindata[i])
        elif way == 1:
            dis = cosdist(dataline, traindata[i])
        tag = traindata[i][10]
        temp = np.array([tag, dis])
        if topk[k - 1, 1] < 0 :
            insert(topk, temp, k)
        elif dis < topk[k - 1, 1] :
            insert(topk, temp, k)
    #print(topk)
    cls = getmost(topk, k)
    return cls


if __name__ == "__main__" :
    dataline = []
    traindata = []
    fr = open("traindata.txt", "r")
    fw = open("output.txt", "w+")
    for i in range(4409):
        str0 = fr.readline().split(" ")
        lst = []
        for j in range(11):
            lst.append(float(str0[j]))
        traindata.append(lst)
    traindata = np.array(traindata)
    for way in range(2):    #way0 as euc-dist, way1 as cos-dist
        for k in range(3, 10, 2):
            right = 0
            wrong = 0
            frt = open("testdata.txt", "r")
            for i in range(488):
                str0 = frt.readline().split(" ")
                lst = []
                for j in range(11):
                    lst.append(float(str0[j]))
                dataline = lst
                dataline = np.array(dataline)
                test = int(classify(dataline, traindata, 4409, k, way))
                real = dataline[10]
                if test == real:
                    right += 1
                else :
                    wrong += 1
            acc = float(right / (right + wrong))
            fw.write(str(k)+ " " + str(acc) + "\n")
            frt.close()
    fr.close()
    fw.close()
