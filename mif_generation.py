# Import Libraries
import sys
import pandas as pd
import numpy as np
import random
import operator
import matplotlib.pyplot as plt
from collections import defaultdict

#Reading the CSV file into a dataframe
df = pd.read_csv('Accident_Information.csv')

#Converting the dataframe to a Numpy array for increased computation speed
df_np = np.array(df)

#Converting Categorical Variables to Numerical Encodings
df['1st_Road_Class'] = df['1st_Road_Class'].astype('category').cat.codes
df['1st_Road_Number'] = df['1st_Road_Number'].astype('category').cat.codes
df['Accident_Severity'] = df['Accident_Severity'].astype('category').cat.codes
df['Day_of_Week'] = df['Day_of_Week'].astype('category').cat.codes
df['Did_Police_Officer_Attend_Scene_of_Accident'] = df['Did_Police_Officer_Attend_Scene_of_Accident'].astype('category').cat.codes
df['Junction_Control'] = df['Junction_Control'].astype('category').cat.codes
df['Junction_Detail'] = df['Junction_Detail'].astype('category').cat.codes
df['Light_Conditions'] = df['Light_Conditions'].astype('category').cat.codes
df['Local_Authority_(District)'] = df['Local_Authority_(District)'].astype('category').cat.codes
df['Pedestrian_Crossing-Human_Control'] = df['Pedestrian_Crossing-Human_Control'].astype('category').cat.codes
df['Pedestrian_Crossing-Physical_Facilities'] = df['Pedestrian_Crossing-Physical_Facilities'].astype('category').cat.codes
df['Police_Force'] = df['Police_Force'].astype('category').cat.codes
df['Road_Surface_Conditions'] = df['Road_Surface_Conditions'].astype('category').cat.codes
df['Road_Type'] = df['Road_Type'].astype('category').cat.codes
df['Accident_Severity'] = df['Accident_Severity'].astype('category').cat.codes
df['Speed_limit'] = df['Speed_limit'].astype('category').cat.codes
df['Urban_or_Rural_Area'] = df['Urban_or_Rural_Area'].astype('category').cat.codes
df['Weather_Conditions'] = df['Weather_Conditions'].astype('category').cat.codes
df['Year'] = df['Year'].astype('category').cat.codes

#Creating Dictionaries to store the Ordered Lists as well as the MIF data
orderedList = defaultdict(list)
orderedListDistances = defaultdict(list)
prunedOrderedList = defaultdict(list)
prunedOrderedListDistances = defaultdict(list)
metricInvertedFile = defaultdict(list)

#Function to select 1000 random reference points
def selectReferencePoints():
    referencePoints = []
    referencePoints = random.sample(range(0, len(df)), 1000)
    referencePoints.sort()
    return referencePoints

#Quick Sort Helper Function
def partition(arr, arr2, low, high):
    i = low-1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
            arr2[i], arr2[j] = arr2[j], arr2[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    arr2[i+1], arr2[high] = arr2[i+1], arr2[high]
    return i+1

#Quick Sort Function
def quickSort(arr, arr2, low, high):
    if low < high:
        pi = partition(arr, arr2, low, high)

        quickSort(arr, arr2, low, pi-1)
        quickSort(arr, arr2, pi+1, high)

#Function to sort the created Ordered Lists
def sortOrderedList(start, end):
    for i in range(start,end):
        if (i%10000) == 0:
            print("Progress = "+str((i/100000)*100)+"%")
        quickSort(orderedListDistances['o'+str(i)], orderedList['o'+str(i)], 0, len(orderedListDistances['o'+str(i)]) - 1)

#Function to Prune Ordered Lists to required size
def pruneOrderedList(size, start, end):
    for i in range(start, end):
        prunedorderedList['o'+str(i)] = orderedList['o'+str(i)][:size]
        prunedOrderedListDistances['o'+str(i)] = orderedListDistances['o'+str(i)][:size]

#Function to create MIF 
def produceMif(start, end):
    for i in range(len(referencePoints)):
        if (i%10) == 0:
        	print("Progress = "+str((i/1000)*100)+"%")
        for j in range(start, end):
            try:
                index = prunedOrderedList['o'+str(j)].index('r'+str(referencePoints[i]))
                metricInvertedFile['r'+str(referencePoints[i])].append(['o'+str(j), index+1])
            except:
                continue

#Save Generated MIF Files to txt file
def saveMiftoTxt(i):
    f = open("mifAccidentInformation"+str(i)+".txt", "x")
    for key, value in metricInvertedFile.items():
        f.write(str(key) + ':' + str(value) + '\n\n')

def calculateDistances(start, end):
    for i in range(start, end):
        if (i%1000) == 0:
            print("Progress = "+str((i/100000)*100)+"%")
        for j in (referencePoints):
            distance = 0
            distance = np.sum(np.absolute(np.subtract(df_np[i], df_np[j])))
            orderedListDistances['o'+str(i)].append(distance)
            orderedList['o'+str(i)].append('r'+str(j))


#Select Reference Points
referencePoints = selectReferencePoints()

#Calling functions on 10 parts of the dataset (each of 100,000 rows)
#This will create 10 MIF files
start, end = 0
for i in range(0, 10):
	start = i*100000
	end = (i+1)*100000

	#Create Ordered Lists based on Spearmna Footrule Distance
	calculateDistances(start, end)
	#Sort Ordered Lists
	sortOrderedList(start, end)
	#Prune Ordered List
	pruneOrderedList(10, start, end)
	#Produce MIF Dictionary
	produceMif(start, end)
	#Save MIF File to TXT File
	saveMiftoTxt(i+1)

#Code to open all 10 MIF files and merge into 1 MIF file
mif_dict = defaultdict(list)

for i in range(1, 11):
	with open("mifAccidentInformation"+str(i)+".txt") as f:
	    for i, line in enumerate(f):
	        if i%2 == 0
	        (key, val) = line.split(':')
	        if key in d.keys():
	            d[str(key)].append([val])
	        else:
	            d[str(key)] = [val]

#Some extra file cleaning
keys = []
for i in mif_dict.keys():
    keys.append(i)

for i in keys:
    for word, initial in {"[\"[" : "[", "\'" : "", "]n\"" : "", "]]]\n" : "]]", "]]\\n\"]]\n" : "]]", "]]," : "],", "]]\\n\"," : "]," , ", [[" : ", [" , "]]\n" : "]]" , "]]\\n\"]" : "]"}.items():
        mif_dict[str(i)] = mif_dict[str(i)].replace(word, initial)

#Save final MIF file after merging into 1 MIF File
f = open("mifAccidentInformationresult_final.txt", "x")
    for key, value in mif_dict.items():
        f.write(str(key) + ':' + str(value) + '\n\n')