import re
import numpy
import matplotlib
import time

matplotlib.use('Agg')
from matplotlib import pyplot as plt

##Setup


def viewdictsetup(dict1, list1, list2, list3, list4, list5):
    for rows1 in list1:
        try: 
            if rows1[0] not in dict1:
                dict1[rows1[0]] = [rows1[1]]
        except: 
            if rows1[0] not in dict1:
                dict1[rows1[0]] = ['0']
                continue
    #print(dict1) 
    for rows2 in list2:
            if rows2[0] not in dict1:
                try:
                    # print(rows2[0])
                    # print(rows2[1])
                    dict1[rows2[0]] = [rows2[1]]
                except:
                    dict1[rows2[0]] = ['0']
                    continue
            
            if rows2[0] in dict1: 
                try:
                    dict1[rows2[0]] = dict1[rows2[0]] + [rows2[1]]
                    continue
                
                except:
                    dict1[rows2[0]] = dict1[rows2[0]] + ['0']
                    continue
    
    for rows3 in list3:
            if rows3[0] not in dict1:
                try:
                    # print(rows2[0])
                    # print(rows2[1])
                    dict1[rows3[0]] = [rows3[1]]
                except:
                    dict1[rows3[0]] = ['0']
                    continue
                
            
            if rows3[0] in dict1: 
                try:
                    dict1[rows3[0]] = dict1[rows3[0]] + [rows3[1]]
                    continue
                
                except:
                    dict1[rows3[0]] = dict1[rows3[0]] + ['0']
                    continue
        
    for rows4 in list4:
            if rows4[0] not in dict1:
                try:
                    # print(rows2[0])
                    # print(rows2[1])
                    dict1[rows4[0]] = [rows4[1]]
                except:
                    dict1[rows4[0]] = ['0']
                    continue
                
            
            if rows4[0] in dict1: 
                try:
                    dict1[rows4[0]] = dict1[rows4[0]] + [rows4[1]]
                    continue
                
                except:
                    dict1[rows4[0]] = dict1[rows4[0]] + ['0']
                    continue
        
    for rows5 in list5:
            if rows5[0] not in dict1:
                try:
                    # print(rows2[0])
                    # print(rows2[1])
                    dict1[rows5[0]] = [rows5[1]]
                except:
                    dict1[rows5[0]] = ['0']
                    continue
                
            
            if rows5[0] in dict1: 
                try:
                    dict1[rows5[0]] = dict1[rows5[0]] + [rows5[1]]
                    continue
                
                except:
                    dict1[rows5[0]] = dict1[rows5[0]] + ['0']
                    continue
        
    return dict1

def commentdictsetup(dict2, list1, list2, list3, list4, list5):
    for rows1 in list1:
        try:
            if rows1[0] not in dict2:
                dict2[rows1[0]] = [rows1[4]]
        except: 
            if rows1[0] not in dict2:
                dict2[rows1[0]] = ['0']
                continue
        
    for rows2 in list2:
            if rows2[0] not in dict2:
                try:
                    dict2[rows2[0]] = [rows2[4]]
                except:
                    dict2[rows2[0]] = ['0']
                    
            if rows2[0] in dict2: 
                try:
                    dict2[rows2[0]] = dict2[rows2[0]] + [rows2[4]]
                    continue
                
                except:
                    dict2[rows2[0]] = dict2[rows2[0]] + ['0']
                    continue
    
    for rows3 in list3:
            if rows3[0] not in dict2:
                try:
                    dict2[rows3[0]] = [rows3[4]]
                except:
                    dict2[rows3[0]] = ['0']
                
            if rows3[0] in dict2: 
                try:
                    dict2[rows3[0]] = dict2[rows3[0]] + [rows3[4]]
                    continue
                
                except:
                    dict2[rows3[0]] = dict2[rows3[0]] + ['0']
                    continue
    
    for rows4 in list4:
            if rows4[0] not in dict2:
                try:
                    dict2[rows4[0]] = [rows4[4]]
                except:
                    dict2[rows4[0]] = ['0']
                
            if rows4[0] in dict2: 
                try:
                    dict2[rows4[0]] = dict2[rows4[0]] + [rows4[4]]
                    continue
                
                except:
                    dict2[rows4[0]] = dict2[rows4[0]] + ['0']
                    continue
    
    for rows5 in list5:
            if rows5[0] not in dict2:
                try:
                    dict2[rows5[0]] = [rows5[4]]
                except:
                    dict2[rows5[0]] = ['0']
                
            if rows5[0] in dict2: 
                try:
                    dict2[rows5[0]] = dict2[rows5[0]] + [rows5[4]]
                    continue
                
                except:
                    dict2[rows5[0]] = dict2[rows5[0]] + ['0']
                    continue
    
    return dict2
    
def ratingdictsetup(dict3, list1, list2, list3, list4, list5):
    for rows1 in list1:
        try:
            if rows1[0] not in dict3:
                dict3[rows1[0]] = [rows1[2]]
        except: 
            if rows1[0] not in dict3:
                dict3[rows1[0]] = ['0']
                continue
        
    for rows2 in list2:
            if rows2[0] not in dict3:
                try:
                    dict3[rows2[0]] = [rows2[2]]
                    continue
                except:
                    dict3[rows2[0]] = ['0']
                    continue
            
            if rows2[0] in dict3: 
                try:
                    dict3[rows2[0]] = dict3[rows2[0]] + [rows2[2]]
                    continue
                
                except:
                    dict3[rows2[0]] = dict3[rows2[0]] + ['0']
                    continue
    
    for rows3 in list3:
            if rows3[0] not in dict3:
                try:
                    dict3[rows3[0]] = [rows3[2]]
                    continue
                except:
                    dict3[rows3[0]] = ['0']
                    continue
                
            
            if rows3[0] in dict3: 
                try:
                    dict3[rows3[0]] = dict3[rows3[0]] + [rows3[2]]
                    continue
                
                except:
                    dict3[rows3[0]] = dict3[rows3[0]] + ['0']
                    continue
    
    for rows4 in list4:
            if rows4[0] not in dict3:
                try:
                    dict3[rows4[0]] = [rows4[2]]
                    continue
                except:
                    dict3[rows4[0]] = ['0']
                    continue
                
            
            if rows4[0] in dict3: 
                try:
                    dict3[rows4[0]] = dict3[rows4[0]] + [rows4[2]]
                    continue
                
                except:
                    dict3[rows4[0]] = dict3[rows4[0]] + ['0']
                    continue
    
    for rows5 in list5:
            if rows5[0] not in dict3:
                try:
                    dict3[rows5[0]] = [rows5[2]]
                    continue
                except:
                    dict3[rows5[0]] = ['0']
                    continue
                
            
            if rows5[0] in dict3: 
                try:
                    dict3[rows5[0]] = dict3[rows5[0]] + [rows5[2]]
                    continue
                
                except:
                    dict3[rows5[0]] = dict3[rows5[0]] + ['0']
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

def viewcountorganize(viewingdict, toptenlist, bottomtenlist):
    percentchangestore = []
    inverseviewpercent = dict()
    keylist = list(viewingdict.keys())
    
    for key in keylist:
        tempkeylist = viewingdict[key]
        
        try:
            percent = ((int(tempkeylist[4])-int(tempkeylist[0]))/ (int(tempkeylist[0])))*100
            if percent == -100.0:
                percent = 0
            
            if percent != 0:
                percentchangestore.append(percent)
                inverseviewpercent[percent] = key
        
        except: 
            percent = 0
            continue
    
    print(inverseviewpercent)
    newpercentchangestore = sorted(percentchangestore)
    print(newpercentchangestore)
    
    listlength = len(newpercentchangestore)
    topten = newpercentchangestore[(listlength - 10):listlength]
    
    #print(topten)
    for value in topten:
        for key in inverseviewpercent:
            if key == value:
                toptenlist.append([value,inverseviewpercent[key]])
                
    
    bottomten = newpercentchangestore[0:10]
    
    #print(bottomten)
    for value in bottomten:
        for key in inverseviewpercent:
            if key == value:
                bottomtenlist.append([value,inverseviewpercent[key]])

    return (toptenlist, bottomtenlist)

## Begin Code ##
toptenlist = []
bottomtenlist = []

print('Welcome to the Youtube Web Crawl Analyzer.')
time.sleep(2)
print("1. Choose Data \n")
print("2. See Help \n")
userchoice1 = input("Please choose an option: \n")
if userchoice1 == "1":
    #First crawl selection
    time.sleep(1)
    print('Prepare 5 data files for analysis.')
    crawl1 = input('What data file do you declare as the first web crawl? \n')
    with open(crawl1) as d:
        data_lines = d.readlines()
    
    # Second crawl selection
    crawl2 = input('What data file do you declare as the second web crawl? \n')
    with open(crawl2) as d2:
        data_lines_2 = d2.readlines()
    
    #Third crawl selection
    crawl3 = input('What data file do you declare as the third web crawl? \n')
    with open(crawl3) as d3:
        data_lines_3 = d3.readlines()
    
    #Fourth Crawl selection
    crawl4 = input('What data file do you declare as the fourth web crawl? \n')
    with open(crawl4) as d4:
        data_lines_4 = d4.readlines()
    
    #Fifth Crawl selection
    crawl5 = input('What data file do you declare as the fifth web crawl? \n')
    with open(crawl5) as d5:
        data_lines_5 = d5.readlines()
    
    view_list = []
    view_list_2 = []
    view_list_3 = []
    view_list_4 = []
    view_list_5 = []
    
    for rows1 in data_lines: #make function later
        splitList = rows1.split()
        #print(splitList)
        view_list.append(splitList)
    
    for rows2 in data_lines_2:
        splitList2 = rows2.split()
        view_list_2.append(splitList2)
    
    for rows3 in data_lines_3:
        splitList3 = rows3.split()
        view_list_3.append(splitList3)
    
    for rows4 in data_lines_4:
        splitList4 = rows4.split()
        view_list_4.append(splitList4)
    
    for rows5 in data_lines_5:
        splitList5 = rows5.split()
        view_list_5.append(splitList5)
    
    viewdict = dict()
    commentdict = dict()
    ratingdict = dict()
    
    #print(view_list_2)
    
    
    viewdictsetup(viewdict, view_list, view_list_2, view_list_3, view_list_4, view_list_5)    
    commentdictsetup(commentdict, view_list, view_list_2, view_list_3, view_list_4, view_list_5)
    ratingdictsetup(ratingdict, view_list, view_list_2, view_list_3, view_list_4, view_list_5)
    
    #print(viewdict)
    #print(commentdict)
    #print(ratingdict)
    
    print('1. Percent Change of Viewcount over time')
    print('2. Ranking of the top ten fastest growing videos over time')
    print('3. Ranking of the top ten slowest growing videos over time')
    print('4. Distribution of Rating count')
    print('5. Distribution of Comment count')
    userchoice2 = input('Select a method of analysis.')
    
    ## Find rate of viewcount growth
    #For now, we can do percentage increase
    
    viewrankdict = dict()
    # keylist = list(viewdict.keys())
    
    # percentchangestore = []
    # inverseviewpercent = dict()
    
    # for key in keylist:
    #     tempkeylist = viewdict[key]
        
    #     try:
    #         percent = ((int(tempkeylist[4])-int(tempkeylist[0]))/ (int(tempkeylist[0])))*100
    #         if percent == -100.0:
    #             percent = 0
            
    #         if percent != 0:
    #             percentchangestore.append(percent)
    #             inverseviewpercent[percent] = key
        
    #     except: 
    #         percent = 0
    #         continue
    
    # #print(inverseviewpercent)
    # newpercentchangestore = sorted(percentchangestore)
    # #print(newpercentchangestore)
    
    # listlength = len(newpercentchangestore)
    # topten = newpercentchangestore[(listlength - 10):listlength]
    # toptenlist = []
    # #print(topten)
    # for value in topten:
    #     for key in inverseviewpercent:
    #         if key == value:
    #             toptenlist.append([value,inverseviewpercent[key]])
                
    # #print(toptenlist)
    
    
    # bottomten = newpercentchangestore[0:10]
    # bottomtenlist = []
    # #print(bottomten)
    # for value in bottomten:
    #     for key in inverseviewpercent:
    #         if key == value:
    #             bottomtenlist.append([value,inverseviewpercent[key]])
    
    viewcountorganize(viewdict, toptenlist, bottomtenlist)
    print(toptenlist)
    print(bottomtenlist)
    
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