import re

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
                    print('hi')
                    continue
                
                except:
                    dict1[rows2[0]] = dict1[rows2[0]] + ['0']
                    print('boo')
                    continue
        
        # except:        
        #     if rows2[0] not in dict1:
        #         dict1[rows2[0]] = dict1[rows2[0]] + ['0']
        #         print('hi')
        #     continue
    
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
        try:
            if rows4[0] not in dict2:
                dict2[rows4[0]] = [rows4[4]]
            
            if rows4[0] in dict2: 
                #print(rows4[1])
                #print(dict2[rows4[0]])
                dict2[rows4[0]] = dict2[rows4[0]] + [rows4[4]]
                
        
        except:        
            if rows4[0] not in dict2:
                dict2[rows4[0]] = dict2[rows4[0]].append('0')
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
        try:
            if rows6[0] not in dict3:
                dict3[rows6[0]] = [rows6[2]]
            
            if rows6[0] in dict3: 
                #print(rows4[1])
                #print(dict2[rows4[0]])
                dict3[rows6[0]] = dict3[rows6[0]] + [rows6[2]]
                
        
        except:        
            if rows6[0] not in dict3:
                dict3[rows6[0]] = dict3[rows6[0]].append('0')
            continue
    
    return dict3

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

print(viewdict)
#print(commentdict)
#print(ratingdict)

## Find rate of viewcount growth
#For now, we can do percentage increase

viewrankdict = dict()
lst = list(viewdict.keys())

# for key in lst:
#     templist = viewdict[key]
#     try:
#         percent = ((int(templist[1])-int(templist[0]))/ (int(templist[0])))*100
#     #print(viewdict[key][1])
#         print(percent)
        
    
#     except:
#         print('Missed')
#         continue