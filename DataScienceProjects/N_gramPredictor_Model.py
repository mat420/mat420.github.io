#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pm4py


# In[2]:


import pandas as pd


# In[3]:


from pm4py.objects.log.importer.xes import importer as xes_importer
log = xes_importer.apply('D:\Documents\spa\BPI Challenge 2018.xes\BPI Challenge 2018.xes')


# In[4]:


log[0][0]


# In[5]:


#filtering payment application in activity

data = []
for d in range(0,1000):
    mydata = []
    for n in range(0,len(log[d])):
        mydata.append(log[d][n]['activity'])
        data.append(mydata)
data


# In[95]:


import seaborn as sns
sns.set()
sns.set_style("whitegrid")
import random
import matplotlib.pyplot as plt
def n_gram_predictor(latest_value, n, process):
    n_gram = []
    next_process = []
    next_prob = []
    
    if len(latest_value) >= n:
        for a in range(1, n + 1):
            present_val = latest_value[-a:]
            for b in range(len(process)):
                c = 0
                while c < len(process[b]) - len(present_val) + 1:
                    if present_val == process[b][c:c + len(present_val)]:
                        if c + len(present_val) < len(process[b]):
                            next_process.append(process[b][c + len(present_val)])
                    c += 1
                        
        if next_process:
            for element in set(next_process):
                probability_element = next_process.count(element) / len(next_process)
                next_prob.append([a, element, probability_element])

            data = {"n-gram": [p[0] for p in next_prob], "next process": [p[1] for p in next_prob], "probability": [p[2] for p in next_prob]}
            df = pd.DataFrame(data)
            print(df)
            if next_process:
                main_data = df["probability"]
                n_gram_values = df["n-gram"].unique()
                colors = ["red", "blue", "green", "orange", "purple"]
                random.shuffle(colors)
                color_map = {n: color for n, color in zip(n_gram_values, colors)}
                color_list = [color_map[n] for n in df["n-gram"]]
                next_process_values = df["next process"].unique()
                bar_locations = range(len(next_process_values))
                bar_heights = [df[df["next process"] == next_process]["probability"].sum() for next_process in next_process_values]
                plt.bar(bar_locations, bar_heights, color=color_list)
                plt.xticks(bar_locations, next_process_values,fontsize=12)
                plt.xlabel("Next Process",fontsize=20)
                plt.ylabel("Probability",fontsize=20)
                plt.title("Next Process Probability Plot",fontsize=20)
                plt.tick_params(axis='both', which='major', labelsize=12)
                plt.show()
                
                plt.rcParams['figure.figsize'] = (45, 20)
        else:
            print("No next process available")
    else:
        print("Enter n less than present process length")


# In[96]:


current_instances = ['begin editing','save','insert document']
n_gram_predictor(current_instances,3,data)


# In[97]:


n_gram_predictor(current_instances,2,data)


# In[98]:


n_gram_predictor(current_instances,1,data)


# In[46]:




