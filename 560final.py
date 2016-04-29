import re
import numpy
import matplotlib
import time
from setup import *


## Begin Code ##
toptenlist = []
bottomtenlist = []

while True:
    print('Welcome to the Youtube Web Crawl Analyzer.') #Initial Menu
    time.sleep(2)
    print("1. Choose Data \n")
    print('2. Help \n')
    print('3. Exit. \n')
    userchoice1 = input("Please choose an option: \n")
    
    try:
        if userchoice1.strip() == "3": #Choice cases
            print('Application has exited.')
            break #For ending
        
        if userchoice1.strip() == "2":
            apphelp() #For calling help
        
        if userchoice1.strip() == "1": #Choosing data
            #First crawl selection
            time.sleep(1)
            print('Prepare 5 data files for analysis.') #5 inputs are necessary! Otherwise restart.
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
            
            for rows1 in data_lines: #reading each file.
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
            viewrankdict = dict()
            
            
            
            viewdictsetup(viewdict, view_list, view_list_2, view_list_3, view_list_4, view_list_5)    #Dictionary setups
            commentdictsetup(commentdict, view_list, view_list_2, view_list_3, view_list_4, view_list_5)
            ratingdictsetup(ratingdict, view_list, view_list_2, view_list_3, view_list_4, view_list_5)
            viewcountorganize(viewdict, toptenlist, bottomtenlist, viewrankdict) #Doing one-time calculations.
            
            while True:
                print('1. Percent Change of selected Video Viewcount over time')
                print('2. Ranking of the top ten fastest growing videos over time and line graph of top fastest and 10th fastest growing videos')
                print('3. Ranking of the top ten slowest growing videos over time and line graph of top slowest and 10th slowest growing videos')
                print('4. Distribution of Rating count')
                print('5. Distribution of Comment count')
                print('6. Help')
                print('7. Exit')
                userchoice2 = input('Select a method of analysis.\n')
                
                
                try: #Same case as the last while loop.
                    if userchoice2.strip() == "1": #Percent change, and graphing input
                        videoinput = input("Give a video ID for the percent change in views.\n")
                        for keys in viewrankdict:
                            if videoinput.strip() == keys:
                                print("The overall percent change of the view is: " + str(round(viewrankdict[keys])) + "% " + "\n")
                                graphinput(videoinput, viewdict)
                        
                    
                    if userchoice2.strip() == "2": #Making top ten list/graphing
                        maketoptenlist(toptenlist, viewdict)
                    
                    if userchoice2.strip() == "3":
                        makebottomtenlist(bottomtenlist, viewdict) #Making bottom ten list/graphing
                    
                    ## Histograms
                    
                    #Here to graph the rating distribution
                    
                    if userchoice2.strip() == "4": #Making Histogram for ratings
                        ratinghistogramsetup(ratingdict)
                    
                    if userchoice2.strip() == "5":
                    # Graph Comment count distribution
                        commentdicthistsetup(commentdict)
                    
                    if userchoice2.strip() == "6": #Calling help
                        apphelp()
                    
                    if userchoice2.strip() == "7": #Ending loop and going back to the main menu.
                        print('Thank you for using this application. Going back to main menu\n')
                        break
    
                except:
                    print('Invalid Input. Please Reassess and Try Again.\n')
    except:
        print('Invalid Input. Please Reassess and Try Again.\n')