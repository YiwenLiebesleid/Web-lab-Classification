import numpy as np

def loadDataSet(filename):
    dataMat = []
    labelMat = []
    fr = open(filename, "r")
    for line in fr.readlines():
        lineA = line.strip().split(" ")
        dataMat.append([float(lineA[0]),float(lineA[1]),float(lineA[2]),float(lineA[3]),
                        float(lineA[4]),float(lineA[5]),float(lineA[6]),float(lineA[7]),
                        float(lineA[8]),float(lineA[9])])
        if int(lineA[10]) >= 6:
            labelMat.append(1)
        else:
            labelMat.append(0)
    #print(dataMat)
    return dataMat, labelMat

def sigmoid(x):
    y = 1.0 / (1.0 + np.exp(-x))
    #print(y)
    return y

def gradAscent(dataMatIn, classLabels):
    dataMat = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()
    m, n = np.shape(dataMat)
    alpha = 0.01
    cycle = 1100
    weights = np.ones((n,1))
    sum = 0
    for k in range(cycle):
        h = sigmoid(dataMat * weights)
        error = (labelMat - h)
        #print(h)
        weights = weights + alpha * dataMat.transpose() * error
        if k == cycle - 1:
            for i in range(m):
                sum += error[i,0]
            sum /= m
    print("Train Error: " + str(sum))
    return weights

def testAns(testMat, weights, testlabel):
    dataMat = np.mat(testMat)
    h = sigmoid(dataMat * weights)
    right = 0
    wrong = 0
    n = np.shape(dataMat)[0]
    #print(testlabel)
    for i in range(n):
        #print(h[i,0])
        if h[i,0] == testlabel[i]:
            right += 1
        else:
            wrong += 1
    acc = float(right / (right + wrong))
    return acc

if __name__ == "__main__" :
    dataMat, labelMat = loadDataSet("traindata.txt")
    wei = gradAscent(dataMat, labelMat)

    testMat, testlabel = loadDataSet("testdata.txt")
    acc = testAns(testMat,wei,testlabel)
    print("Accuracy: " + str(acc))
