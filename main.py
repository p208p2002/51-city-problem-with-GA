from core import *
from plot import *
import random
from collections import Counter
import copy
#initial   
NUM_CITIES =51
DIC = loadDic()
ITER_NUM = 2500
INITIAL_POPULATION_NUM = 8
CROSSOVER_LEN = 4
MOUTATION_LEVEL = 25 # 10(%) = 0.1

if __name__ == '__main__':
    # generate initial population
    chromosomes = []

    for i in range(INITIAL_POPULATION_NUM):
        chromosomes.append(init(NUM_CITIES))
        c = chromosomes[i]
        print("chromosomes"+str(i),c)
        print("value:",evalu(c,DIC))
    print()

    for NOW_ITER in range(ITER_NUM):
        parentsChromosomes = copy.deepcopy(chromosomes)        
        splitPointStart = random.randint(0,NUM_CITIES - CROSSOVER_LEN)
        splitPointEnd = splitPointStart + CROSSOVER_LEN
        # print("Round:"+str(NOW_ITER))
        
        # 打亂
        random.shuffle(chromosomes)

        # 交配
        for i in range(0,INITIAL_POPULATION_NUM,2):
            # 取出基因
            c1 = chromosomes[i].copy()
            c2 = chromosomes[i+1].copy()
            # 得到切片
            c1Split = c1[splitPointStart:splitPointEnd]
            c2Split = c2[splitPointStart:splitPointEnd]
            # 交換切片
            c1[splitPointStart:splitPointEnd] = c2Split.copy()
            c2[splitPointStart:splitPointEnd] = c1Split.copy()
            # 復位
            c1d = dict(Counter(c1))
            c2d = dict(Counter(c2))
            
            c1r = findRepeat(c1d,NUM_CITIES)
            c2r = findRepeat(c2d,NUM_CITIES)
            
            c1rb = returnBack(c1r,c1)
            c2rb = returnBack(c2r,c2)

            c1,c2 = swapBack(c1,c1rb,c2,c2rb)
            chromosomes[i] = c1.copy()
            chromosomes[i+1] = c2.copy()
        
        # 得到交配完成chromosomes
        childChromosomes = copy.deepcopy(chromosomes)
        chromosomes = []
        chromosomes = parentsChromosomes+childChromosomes

        # 突變
        for i,c in enumerate(chromosomes):
            newC = mutation(c,MOUTATION_LEVEL) 
            chromosomes[i] = newC
        
        # 排序結果
        chromosomesObjs = []
        for c in chromosomes:
            chromosomesObjs.append((c,evalu(c,DIC)))
        chromosomesObjs.sort(key = lambda x:x[1],reverse=False)
        
        # 選出下一代
        chromosomes = []
        for i,c in enumerate(chromosomesObjs):            
            chromosomes.append(c[0])        
        chromosomes = chromosomes[0:INITIAL_POPULATION_NUM]
        
        # 印出本世代最高分數
        print("R:"+str(NOW_ITER),evalu(chromosomes[0],DIC))
    
    print()
    print("FINAL PATH:\n",chromosomes[0])
    print("FINAL VAL:\n",evalu(chromosomes[0],DIC))
    showPlot(chromosomes[0],'Travel Path')
        