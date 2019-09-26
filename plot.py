import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
from core import *

def showPlot(PATH_SEQ):
    # load
    DIC = loadDic()
    with open('./eil51.txt','r') as f:
        eil51 = f.read()
    eil51 = eil51.split("\n")

    # x y
    x=[]
    y=[]
    for i in eil51:
        newi = i.split(" ")
        x.append(int(newi[1]))
        y.append(int(newi[2]))

    myX = []
    myY = []
    myPath = PATH_SEQ
    print(myPath)
    for i in myPath:
        _x,_y = DIC[i]
        myX.append(_x)
        myY.append(_y)
    
    # matplotlib.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.plot(x, y, 'o')
    ax.set_title('Travel Path')
    plt.plot(myX,myY)
    print(myX,myY)
    plt.show()