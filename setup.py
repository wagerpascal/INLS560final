import re
import numpy
import matplotlib
import time

matplotlib.use('Agg')
from matplotlib import pyplot as plt

##Setup


def viewdictsetup(dict1, list1, list2, list3, list4, list5): #Takes Five different compiled lists of lists and organizes the viewcounts per week into a dictionary.
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
                try:
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

def commentdictsetup(dict2, list1, list2, list3, list4, list5): #Takes 5 different lists and organizes the comment counts per week into a dictionary.
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
    
def ratingdictsetup(dict3, list1, list2, list3, list4, list5): #Takes 5 different lists and organizes the ratings per week into a dictionary.
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

def lines(xlabel, ylabel, title, #Formatting taken from https://github.com/txt/evil/blob/master/tex/settingup.md . Unfortunately I found this before we discussed matplotlib. The function setup's credit all goes to ai4se and timm.
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
  
def graphcomparetop(topgraphlist,viewingdict): #Isolating the 1st and 10th ranked videos from the top ten list, and producing a graph from the lines function.
    for keys in viewingdict: #Separate for loops as if statements didn't carry consecutive priority.
        if keys == topgraphlist[0]:
            graph1values = viewingdict[keys]
            graph2 = [keys] + graph1values
            
            
    for keys in viewingdict:
        if keys == topgraphlist[1]:
                graph2values = viewingdict[keys]
                graph3 = [keys] + graph2values
                lines('Weeks', 'Views', 'Fastest Growing Videos- 1st vs. 10th',"toptengraph.png", xsize = 5, ysize = 3, lines = [graph2, graph3]) #See lines function for formatting.
                     

def graphcomparebottom(bottomgraphlist,viewingdict): #Isolating the 1st and 10th ranked videos from the bottom ten list, and producing a graph from the lines function.
    for keys in viewingdict:# Separate for loops as if statements didn't carry consecutive priority.
        if keys == bottomgraphlist[0]:
            graph3values = viewingdict[keys]
            graph4 = [keys] + graph3values
        
    for keys in viewingdict:    
        if keys == bottomgraphlist[1]:
            graph4values = viewingdict[keys]
            graph5 = [keys] + graph4values
            lines('Weeks', 'Views', 'Slowest Growing Videos- 1stvs. 10th', "bottomtengraph.png", xsize = 5, ysize = 3, lines = [graph4, graph5]) #See lines function for formatting.
                    
                    

def graphinput(videoselection,viewingdict): #Carrying the user input
    for keys in viewingdict:
        if videoselection == keys:
            graph1values = viewingdict[keys]
            graph2 = [keys] + graph1values
            lines('Weeks', 'Views', 'Growth of '+ str(videoselection), 'inputgraph.png', xsize = 5, ysize = 3, lines = [graph2]) #See lines function for formatting.

def ratinghistogramsetup(ratingdictionary): #Creating the histogram for ratings.
    avgratinglist = []
    avgratinghist = []
    count1= 0 #Do not need to be global
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    
    for keys in ratingdictionary:
        avgratinglist.append(ratingdictionary[keys])

    avgratinglist = [[(float(j)) for j in i] for i in avgratinglist] #For converting each value into floating values instead of strings. From http://stackoverflow.com/questions/2166577/casting-from-list-of-lists-of-strings-to-list-of-lists-of-ints-in-python
    
    for lists in avgratinglist:
        avgrating = sum(lists)/len(lists) #Calculate average for each list
        avgratinghist.append(avgrating)
                
    
    for values in avgratinghist: #Counting instances
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
            
    displaycount1 = int(count1/400)
    displaycount2 = int(count2/400)
    displaycount3 = int(count3/400)
    displaycount4 = int(count4/400)
    displaycount5 = int(count5/400)

    
    print("\n") #Making Histogram
    print("DISTRIBUTION OF AVERAGE RATINGS")
    print("-----------------------------------")
    print("Each asterisk counts as 400 counts") #May need further tweaking depending on number of data points. Or a function to make it proportional
    print("0 - 1" + ("*"*displaycount1))
    print("1 - 2" + ("*"*displaycount2))
    print("2 - 3" + ("*"*displaycount3))
    print("3 - 4" + ("*"*displaycount4))
    print("4 - 5" + ("*"*displaycount5))
    print("\n")

def commentdicthistsetup(cmtdict): #Creating the comment histogram
    avgcmtlist = []
    avgcmthist = []
    count1= 0 #Do not need to be global or returned
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    
    for keys in cmtdict:
        avgcmtlist.append(cmtdict[keys])

    avgcmtlist = [[(float(j)) for j in i] for i in avgcmtlist] #Taken from http://stackoverflow.com/questions/2166577/casting-from-list-of-lists-of-strings-to-list-of-lists-of-ints-in-python
    
    for lists in avgcmtlist:
        avgcmtcount = sum(lists)/len(lists) #Calculating average
        avgcmthist.append(avgcmtcount)
                
    
    for values in avgcmthist: #Determining counts between ranges. May need further tweaking.
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
            
    displaycount1 = int(count1/30)
    displaycount2 = int(count2/30)
    displaycount3 = int(count3/30)
    displaycount4 = int(count4/30)
    displaycount5 = int(count5/30)
    
    print("\n") #Producing histogram
    print("DISTRIBUTION OF AVERAGE COMMENT COUNTS")
    print("-------------------------------------")
    print("Each Asterisk counts for 30 counts (Units- Comments)")
    print("0 - 100" + ("*"*displaycount1))
    print("100 - 500" + ("*"*displaycount2))
    print("500 - 1000" + ("*"*displaycount3))
    print("1000 - 2000" + ("*"*displaycount4))
    print("3000 - 10000" + ("*"*displaycount5)) #Not a huge problem, but standardizing the column width should be considered in the future
    print("\n")

def viewcountorganize(viewingdict, toptenlist, bottomtenlist, viewrankingdict): #Calculations that are needed ONCE.
    percentchangestore = []
    inverseviewpercent = dict()
    keylist = list(viewingdict.keys())
    
    for key in keylist: #Calculating percent change
        tempkeylist = viewingdict[key]
        
        try:
            percent = ((int(tempkeylist[4])-int(tempkeylist[0]))/ (int(tempkeylist[0])))*100
            if percent == -100.0: #Cutting out the cases where videos disappear
                percent = 0
            
            if percent != 0: #Cutting out cases where videos have no values
                percentchangestore.append(percent)
                inverseviewpercent[percent] = key
        
        except: 
            percent = 0 #Fallback in case != 0 doesn't work.
            continue
    
    newpercentchangestore = sorted(percentchangestore)
    
    listlength = len(newpercentchangestore)
    topten = newpercentchangestore[(listlength - 10):listlength] #Isolating the top ten.
    
    for value in topten:
        for key in inverseviewpercent:
            if key == value:
                toptenlist.append([value,inverseviewpercent[key]]) #Creating list structured as [percent change, video ID].
                
    
    bottomten = newpercentchangestore[0:10] #Same thing as top ten, but for bottom ten.
    
    for values in bottomten:
        for keys in inverseviewpercent:
            if keys == values:
                bottomtenlist.append([value,inverseviewpercent[keys]])
    
    for keys in inverseviewpercent:
        viewrankingdict[inverseviewpercent[keys]] = keys
    

    return (toptenlist, bottomtenlist)


def maketoptenlist(listoftoptennames, viewingdict): #Making top ten list.
    ##Top ten
    n = 1
    print("\n")
    print("TOP TEN \n")
    for names in reversed(listoftoptennames):
        print(str(n) + ": " + names[1])
        n = n+1
    print("\n")
    
    topgraphlist = [listoftoptennames[9][1], listoftoptennames[0][1]] #Isolating 1st and 10th of top ten.
    graphcomparetop(topgraphlist, viewingdict) #Making comparison graph.

def makebottomtenlist(listofbottomtennames, viewingdict): #Making bottom ten list.
     ## Bottom Ten
    m = 1
    print("\n")
    print("BOTTOM TEN \n")
    for names1 in listofbottomtennames:
        print(str(m) + ": " + names1[1])
        m = m+1
    print("\n")
    
    bottomgraphlist = [listofbottomtennames[9][1], listofbottomtennames[0][1]] #Isolating 1st and 10th of bottom ten.
    graphcomparebottom(bottomgraphlist, viewingdict) #Making comparison graph.
    
def apphelp(): #Help menu.
    print("\n")
    print('HELP')
    print('-----------------------')
    print("\n")
    print('> INPUTS')
    print('-----------------------')
    print('The program will only take text files that are organized into the following columns (left to right): video ID, views, video bitrate, ratings, and comment number. The program will take 5 files that were taken weekly. ')
    print('5 files MUST be given.')
    print("\n")
    print("\n")
    print('> DESCRIPTION OF OPTIONS')
    print('-----------------------')
    print('Use numerical inputs for choosing options.')
    print('For Option 1, please input the video ID (only the ID value) into the application. It will tell you the overall percent increase of the video, as well as input a line graph documenting its growth in a file called inputgraph.png.')
    print('For Option 2, the application will automatically output the top ten fastest growing in the terminal, as well as produce a line graph documenting the 1st and 10th ranked videos growth; the resulting file name is toptengraph.png.')
    print('For Option 3, the application will automatically output the top ten slowest growing in the terminal, as well as produce a line graph documenting the 1st and 10th ranked videos growth; the resulting file name is bottomtengraph.png')
    print('For Option 4, the application will take the averages of the ratings of each video over time, and construct a histogram based on the distribution of the average ratings.')
    print('For Option 5, the application will take the averages of the comment counts of each video over time, and construct a histogram based on the distribution of the average comment counts.')
    print('Tip: unless Option 1, try not to enter any rogue inputs.')
    print("\n")
    
    
    
    