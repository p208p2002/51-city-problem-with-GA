# coding: utf-8
import sys
import time
import math
import random

# For GA
def findRepeat(chromosome,num_cities):
    # 找到重複值
    rep = []
    for i in range(num_cities):
        key = i+1
        try:
            if(chromosome[key] == 2):
                rep.append(key)
        except:
            continue
    return rep

def returnBack(chromosome_repeat_list,chromosome):
    # 找到重複值index
    indexs = []
    for target in chromosome_repeat_list:
        for j in range(len(chromosome),0,-1):
            jIndex = j -1
            if chromosome[jIndex] == target:
                indexs.append(jIndex)
                break
    return indexs

def swapBack(c1,c1rb,c2,c2rb):
    # 復位實現
    c1_copy = c1.copy()
    c2_copy = c2.copy()
    for i in range(len(c1rb)):
        c1[c1rb[i]] = c2_copy[c2rb[i]]
        c2[c2rb[i]] = c1_copy[c1rb[i]]
    return (c1,c2)

# From E.G.
def loadDic(dicPath = './eil51.txt'):
    dic={}
    with open(dicPath) as f:
        r=f.read()
        read_line = r.split('\n')              
        
        for i in range(len(read_line)):         
            read_element = read_line[i].split()
            dic[int(read_element[0])] = [int(read_element[1])]
            dic[int(read_element[0])].append(int(read_element[2]))
        
        f.close()
    return dic

def ran(domain): # generate two numbers  that in range to  swap  (ex: if answer is [4,7] means city 4 and city 7 seq. order swap)
    num = []
    first = random.randint(1,domain)
    num.append(first)
    second = random.randint(1,domain)
    ok = 0
    while(ok==0):
        if second != first:
            num.append(second)
            ok = 1
        else:
            second = random.randint(1,domain)
            ok = 0
    return num

def init(num): ## generate init city sequence
    seq = []
    while len(seq) < num:
        temp = random.randint(1,num)
        if temp not in seq:
            seq.append(temp)
            
    return seq

def trans(seq):
    ok_flag=0
    temp = seq[:]
    index = ran(len(seq))
    
    while (ok_flag ==0) : 
        if index[0]!=index[1]:
            ok_flag =1
        else:
            index = ran(len(seq))
        
        
    t = temp[index[0]-1]
    temp[index[0]-1] = temp[index[1]-1]
    temp[index[1]-1] = t
    
    return temp

def distance(axis):
    return math.sqrt(axis[0]*axis[0]+axis[1]*axis[1])

def evalu(seq,dic):
    # 計算seq path 距離
    dist = 0
    for i in range(len(seq)):
        d = [ dic[seq[i]][0]-dic[seq[(i+1)%len(seq)]][0],dic[seq[i]][1]-dic[seq[(i+1)%len(seq)]][1]]
        dist += distance(d)
    return dist

def determine(temp,min_seq,dic):
    if evalu(temp,dic) < evalu(min_seq,dic):
        min_seq = temp[:]
  
    return min_seq,evalu(min_seq,dic)
    
            
def readfile(dic):
    with open('eil51.txt') as f:
        r = f.read()
        read_line = r.split('\n')               
        for i in range(len(read_line)):         
            read_element = read_line[i].split()
            dic[int(read_element[0])] = [int(read_element[1])]
            dic[int(read_element[0])].append(int(read_element[2]))
        f.close()