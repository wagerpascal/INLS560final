import re
import numpy
import matplotlib
import time

matplotlib.use('Agg')
from matplotlib import pyplot as plt

##Setup

def viewdictsetup(dict1, list1, list2):
    for rows1 in list1:
        try: 
            if rows1[0] not in dict1:
                dict1[rows1[0]] = [rows1[1]]
        except: 
            if rows1[0] not in dict1:
                dict1[rows1[0]] = ['0']
                continue
     
    for rows2 in list2:
            if rows2[0] not in dict1:
                dict1[rows2[0]] = [rows2[1]]
                
            
            if rows2[0] in dict1: 
                try:
                    dict1[rows2[0]] = dict1[rows2[0]] + [rows2[1]]
                    continue
                
                except:
                    dict1[rows2[0]] = dict1[rows2[0]] + ['0']
                    continue
        
        
    return dict1

def commentdictsetup(dict2, list3, list4):
    for rows3 in list3:
        try:
            if rows3[0] not in dict2:
                dict2[rows3[0]] = [rows3[4]]
        except: 
            if rows3[0] not in dict2:
                dict2[rows3[0]] = ['0']
                continue
        
    for rows4 in list4:
            if rows4[0] not in dict2:
                dict2[rows4[0]] = [rows4[4]]
                
            
            if rows4[0] in dict2: 
                try:
                    dict2[rows4[0]] = dict2[rows4[0]] + [rows4[4]]
                    continue
                
                except:
                    dict2[rows4[0]] = dict2[rows4[0]] + ['0']
                    continue
    
    return dict2
    
def ratingdictsetup(dict3, list5, list6):
    for rows5 in list5:
        try:
            if rows5[0] not in dict3:
                dict3[rows5[0]] = [rows5[2]]
        except: 
            if rows5[0] not in dict3:
                dict3[rows5[0]] = ['0']
                continue
        
    for rows6 in list6:
            if rows6[0] not in dict3:
                dict3[rows6[0]] = [rows6[2]]
                
            
            if rows6[0] in dict3: 
                try:
                    dict3[rows6[0]] = dict3[rows6[0]] + [rows6[2]]
                    continue
                
                except:
                    dict3[rows6[0]] = dict3[rows6[0]] + ['0']
                    continue
    
    return dict3

def lines(xlabel, ylabel, title,
          f,   
          xsize=5,ysize=5,lines=[]): 
  width = len(lines[0][1:])
  xs = [x for x in range(1,width+1)] 
  plt.figure(figsize=(xsize,ysize))  
  plt.xlabel(xlabel)
  plt.ylabel(ylabel) 
  for line in lines: 
    plt.plot(xs,  line[1:],  
                 label = line[0])   

  plt.locator_params(nbins=len(xs)) 
  plt.title(title)
  plt.legend()
  plt.tight_layout()                
  plt.savefig(f)
  
def graphcomparetop(topgraphlist,viewingdict, i):
    for keys in viewingdict:
        for videoid in topgraphlist:
            if keys == videoid:
                graph1values = viewdict[keys]
                graph2 = [keys] + graph1values
                i = i+ 1
                if i == 1:
                    graph2values = viewdict[keys]
                    graph3 = [keys] + graph2values
    
    lines('Weeks', 'Views', 'Compare',"hi.png", xsize = 5, ysize = 3, lines = [graph2, graph3])
    return graph2, graph3

def graphcomparebottom(bottomgraphlist,viewingdict, i):
    for keys in viewingdict:
        for videoid in bottomgraphlist:
            if keys == videoid:
                graph3values = viewdict[keys]
                graph4 = [keys] + graph3values
                i = i+ 1
                if i == 1:
                    graph4values = viewdict[keys]
                    graph5 = [keys] + graph4values
    
    lines('Weeks', 'Views', 'Compare', "bye.png", xsize = 5, ysize = 3, lines = [graph4, graph5])
    return graph4, graph5

def ratinghistogramsetup(ratingdictionary):
    avgratinglist = []
    avgratinghist = []
    count1= 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    
    for keys in ratingdictionary:
        avgratinglist.append(ratingdictionary[keys])

    avgratinglist = [[(float(j)) for j in i] for i in avgratinglist]
    
    for lists in avgratinglist:
        #print(lists)
        avgrating = sum(lists)/len(lists)
        avgratinghist.append(avgrating)
                
    
    for values in avgratinghist:
        if values >= 0 and values < 1:
            count1 = count1 + 1
        if values >= 1 and values < 2:
            count2 = count1 + 1
        if values >= 2 and values < 3:
            count3 = count3 + 1
        if values >= 3 and values < 4:
            count4 = count4 + 1
        if values >= 4 and values < 5:
            count5 = count5 + 1
            
    displaycount1 = int(count1/20)
    displaycount2 = int(count2/20)
    displaycount3 = int(count3/20)
    displaycount4 = int(count4/20)
    displaycount5 = int(count5/20)
    print(count1)
    print(count2)
    
    print("Count1" + ("*"*displaycount1))
    print("Count2" + ("*"*displaycount2))
    print("Count3" + ("*"*displaycount3))
    print("Count4" + ("*"*displaycount4))
    print("Count5" + ("*"*displaycount5))

def commentdicthistsetup(cmtdict): ################
    avgcmtlist = []
    avgcmthist = []
    count1= 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    
    for keys in ratingdict:
        avgcmtlist.append(cmtdict[keys])

    avgcmtlist = [[(float(j)) for j in i] for i in avgcmtlist]
    
    for lists in avgcmtlist:
        #print(lists)
        avgcmtcount = sum(lists)/len(lists)
        avgcmthist.append(avgcmtcount)
                
    
    for values in avgcmthist:
        if values >= 0 and values < 100:
            count1 = count1 + 1
        if values >= 100 and values < 500:
            count2 = count1 + 1
        if values >= 500 and values < 1000:
            count3 = count3 + 1
        if values >= 1000 and values < 2000:
            count4 = count4 + 1
        if values >= 3000 and values < 10000:
            count5 = count5 + 1
            
    displaycount1 = int(count1/10)
    displaycount2 = int(count2/10)
    displaycount3 = int(count3/10)
    displaycount4 = int(count4/10)
    displaycount5 = int(count5/10)
    print(count1)
    print(count2)
    
    print("Count1" + ("*"*displaycount1))
    print("Count2" + ("*"*displaycount2))
    print("Count3" + ("*"*displaycount3))
    print("Count4" + ("*"*displaycount4))
    print("Count5" + ("*"*displaycount5))

## Begin Code ##
print('Welcome to the Youtube Web Crawl Analyzer.')
time.sleep(2)
print("Please choose an option: \n")
print("1. Choice 1 \n")
print("2. Choice 2 \n")
print("3. Choice 3 \n")


print()
with open('data1.txt') as d:
    data_lines = d.readlines()

#new_data = data_lines.replace(" "," ")

with open('data_2.txt') as d2:
    data_lines_2 = d2.readlines()

view_list = []
view_list_2 = []

for row in data_lines: #make function later
    splitList = row.split()
    #print(splitList)
    view_list.append(splitList)

for rowss in data_lines_2:
    splitList2 = rowss.split()
    view_list_2.append(splitList2)

#print(view_list)
#print(view_list_2)

viewdict = dict()
commentdict = dict()
ratingdict = dict()



viewdictsetup(viewdict, view_list, view_list_2)    
commentdictsetup(commentdict, view_list, view_list_2)
ratingdictsetup(ratingdict, view_list, view_list_2)

#print(viewdict)
#print(commentdict)
#print(ratingdict)

## Find rate of viewcount growth
#For now, we can do percentage increase

viewrankdict = dict()
lst = list(viewdict.keys())

testlist = []
inverseviewpercent = dict()

for key in lst:
    templist = viewdict[key]
    
    try:
        percent = ((int(templist[1])-int(templist[0]))/ (int(templist[0])))*100
        if percent == -100.0:
            percent = 0
        
        if percent != 0:
            testlist.append(percent)
            inverseviewpercent[percent] = key
    
    except: 
        percent = 0
        continue

#print(inverseviewpercent)
newtestlist = sorted(testlist)
#print(newtestlist)

listlength = len(newtestlist)
topten = newtestlist[(listlength - 10):listlength]
toptenlist = []
#print(topten)
for value in topten:
    for key in inverseviewpercent:
        if key == value:
            toptenlist.append([value,inverseviewpercent[key]])
            #print(inverseviewpercent[key], value)
#print(toptenlist)

# for value in toptenlist:

bottomten = newtestlist[0:10]
bottomtenlist = []
#print(bottomten)
for value in bottomten:
    for key in inverseviewpercent:
        if key == value:
            bottomtenlist.append([value,inverseviewpercent[key]])

#print(bottomtenlist)

## List outputs

##Top ten
n = 1
print("TOP TEN \n")
for names in reversed(toptenlist):
    print(str(n) + ": " + names[1])
    n = n+1
print("\n")
    
## Bottom Ten
m = 1
print("BOTTOM TEN \n")
for names1 in bottomtenlist:
    print(str(m) + ": " + names1[1])
    m = m+1
    
## Make graphs
toptennamelist = []
bottomtennamelist = []
# print(toptenlist)
for lists in toptenlist:
  toptennamelist.append(lists[1])

for lists in bottomtenlist:
  bottomtennamelist.append(lists[1])

graph1values = []
graph3values = []
#xaxis = ["Weeks", 1,2]

i = 0
j = 0
topgraphlist = [toptennamelist[9], toptennamelist[0]]
bottomgraphlist = [bottomtennamelist[9], bottomtennamelist[0]]

graphcomparetop(topgraphlist, viewdict, i)
graphcomparebottom(bottomgraphlist, viewdict, j)

## Histograms

#Here to graph the rating distribution

ratinghistogramsetup(ratingdict)

# Graph Comment count distribution
commentdicthistsetup(commentdict)