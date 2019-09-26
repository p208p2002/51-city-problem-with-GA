from core import *
import random
from collections import Counter
import copy
#initial   
num_cities =51
min_seq= init(num_cities)
seq = min_seq
temp = []
dic = loadDic()
readfile(dic)
min_dist = 0

ITER_NUM = 10

INITIAL_POPULATION_NUM = 4
CROSSOVER_LEN = 2

if __name__ == '__main__':
    # generate initial population
    chromosomes = []

    for i in range(INITIAL_POPULATION_NUM):
        chromosomes.append(init(num_cities))
        c = chromosomes[i]
        print("chromosomes"+str(i),c)
        print("value:",evalu(c,dic))
    print()


    for NOW_ITER in range(ITER_NUM):
        parentsChromosomes = copy.deepcopy(chromosomes)
        
        splitPointStart = random.randint(0,num_cities - CROSSOVER_LEN)
        splitPointEnd = splitPointStart + CROSSOVER_LEN

        # 交配
        for i in range(0,INITIAL_POPULATION_NUM,2):
            # 取出基因
            c1 = chromosomes[i].copy()
            c2 = chromosomes[i+1].copy()
            # 得到切片
            c1Split = c1[splitPointStart:splitPointEnd].copy()
            c2Split = c2[splitPointStart:splitPointEnd].copy()
            # 交換切片
            c1[splitPointStart:splitPointEnd] = c2Split.copy()
            c2[splitPointStart:splitPointEnd] = c1Split.copy()
            # 復位
            c1d = dict(Counter(c1))
            c2d = dict(Counter(c2))
            
            c1r = findRepeat(c1d,num_cities)
            c2r = findRepeat(c2d,num_cities)
            
            c1rb = returnBack(c1r,c1)
            c2rb = returnBack(c2r,c2)

            c1,c2 = swapBack(c1,c1rb,c2,c2rb)
            chromosomes[i] = c1.copy()
            chromosomes[i+1] = c2.copy()
        
        # 得到交配完成chromosomes
        childChromosomes = copy.deepcopy(chromosomes)
        chromosomes = []
        chromosomes = parentsChromosomes+childChromosomes
        
        # 排序結果
        chromosomesObjs = []
        for c in chromosomes:
            chromosomesObjs.append((c,evalu(c,dic)))
        chromosomesObjs.sort(key = lambda x:x[1],reverse=False)

        # 選出下一代(前x低，距離越小越好)
        bucket = [] # 籤筒
        for i in range(len(chromosomesObjs)):
            # 排序越後面，越多支籤
            for k in range(i+1):
                bucket.append(i+1)
        
        # print(chromosomesObjs[len(chromosomesObjs)-1][1])

        chromosomes = []
        for i,c in enumerate(chromosomesObjs):
            print(c[1])
            chromosomes.append(c[0])
        print("\n")

        
        chromosomes = chromosomes[0:INITIAL_POPULATION_NUM]
        
        # for c in chromosomesObjs:
        #     print(c[0])
        # print("@s")
        # for c in chromosomes:
        #     print(c)
