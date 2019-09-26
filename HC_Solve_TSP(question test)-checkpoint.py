#!/usr/bin/env python
# coding: utf-8

# # Hill Climbing Algorithm 
# 
# ### 原理可參考 https://www.javatpoint.com/hill-climbing-algorithm-in-ai
# <left><img src="hill-climbing-algorithm-in-ai.png" />
# 
# 

# # Step 1: Functions that we will use

# In[1]:


import sys
import time
import math
import random

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
    dist = 0
    for i in range(len(seq)):
        d = [ dic[seq[i]][0]-dic[seq[(i+1)%len(seq)]][0],dic[seq[i]][1]-dic[seq[(i+1)%len(seq)]][1]]
        dist += distance(d)
        
    
    return dist

def determine(temp,min_seq,dic):
    if evalu(temp,dic) < evalu(min_seq,dic):
        min_seq = temp[:]
        print(min_seq, evalu(min_seq,dic))
  
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


# ## function explain and test

# ### 1. ran() function :  generate two numbers  that in range to  swap  (ex: if answer is [4,7] means city 4 and city 7 seq. order swap)

# In[2]:


which2Swap = ran(3)
print("Which cities to swap:", which2Swap)


# ### 2. init(51) function :  generate an initial city sequence

# In[3]:


seq = init(10)
print(seq)


# ### 3 function trans(seq) can swap cities

# In[4]:


new_seq = trans(seq)
print(new_seq) # it swap two random cities


# ### function 4 read file eil5 51 cities
# 

# In[5]:


### function 4 readfile
dic={}
with open('eil51.txt') as f:
    r=f.read()
    read_line = r.split('\n')              
    print('read_line=',read_line)
    print('len of lines=', len(read_line))
    
    for i in range(len(read_line)):         
        read_element = read_line[i].split()
        dic[int(read_element[0])] = [int(read_element[1])]
        dic[int(read_element[0])].append(int(read_element[2]))
    
    print(dic)
    f.close()


# ### function 5 distance evalu determine
# > distance (x,y) to (0,0)

# In[6]:


#diff = (x_diff,y_diff)
#def distance(axis):
#    return math.sqrt(axis[0]*axis[0]+axis[1]*axis[1])

diff=[20,15] #dx,dy
distance_test=distance(diff) 

print('test for diff {}  distance_test:{}'.format(diff,distance_test))

print("==================================================================")

seq_test=[2,1,3,4]
dic_test={1: [1, 10], 2: [71, 2],3:[22,2],4:[60,3]}
print('dic_test[seq[0]][0],dic_test[seq[0]][1]==',dic_test[seq_test[0]][0],dic_test[seq_test[0]][1])
print('dic_test',dic_test)
print('seq_test',seq_test)
print('seq_test distance for evalu(seq,dic):',evalu(seq_test,dic_test))

print("==================================================================")

print("============ test 5 times =======")

for i in range(5):
    temp_test =trans(seq_test)
    print('temp_test',temp_test)
    print('temp_test for evalu(temp_test,dic_temp):',evalu(temp_test,dic_test))
    new_seq = determine(temp_test,seq_test,dic_test)
    print('new_seq=',new_seq)



# 

# # Step 2: Main Function  把所有code 都放在一起
# > 加上 iteration n 次
# 
# > 有比較好的就印出

# In[7]:


#initial   
num_cities =51
global minVal 
minVal=0
global min_seq
min_seq= init(num_cities)
seq = min_seq
temp = []
dic = {}
readfile(dic)
min_dist = 0
iter_num = input('Please enter the iteration:')
iter_num = int(iter_num)

#Execute
import pandas as pd


for i in range(iter_num): # iteration iter_num =10000次看看
    
    temp = trans(seq)
    min_seq, minVal= determine(temp,min_seq,dic)
    

#Output

print('Final sequence:',min_seq)
print('Final distance:',minVal)


# In[ ]:





# In[ ]:




