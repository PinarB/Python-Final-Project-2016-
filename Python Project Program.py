'''
    Input: .txt or .csv file with demographic information for a group (CSV)
    Output: .txt file describing the demographic makeup of the group, percentages of the categories entered
    For more information, see the readme file

    PBarlas    04/23/2016  Creation
'''
import os
import operator

def makelistofdata(file):
    filetoread = file
    values = filetoread.read()
    values = values.replace("\n", ",")
    listofvalues = values.split(",")
    listofvalues = list(map(str.strip, listofvalues))
    filetoread.close()
    return listofvalues

def sliceintolists(categories, biglist):
    n=0
    newdic = {}
    for item in categories:
        key = categories[n]
        value = set(biglist[n::len(categories)])
        newdic[key] = value
        n+=1
    return newdic

def makedicofperc(listofdata):
    n=0
    newdic = dict((x,listofdata.count(x)) for x in set(listofdata))
    for key in newdic:
        totalans=len(restofdata)/len(categorieslist)
        newdic[key] = newdic[key]/totalans*100
    return newdic                       #where Key is subcategory, Value is a tuple (number, percentage) of occurrance

def showresults(finallist):
    print("Demographic makeup of the group surveyed:\n")
    for subcat, perc in finallist:
        if subcat in categoryrefdic["Wage"]:
            print("%4.1f percent of this group earns % %-20s \n" %perc %subcat)
        elif subcat in categoryrefdic["Age"]:
            print("%4.1f percent of this group is aged % %-20s \n" %perc %subcat)
        else:
            print("%4.1f percent of this group is % %-20s \n" %perc %subcat)
    return "End of results!"

def writetofile(outputname, finallist):
    outputfile = open(outputname, "w")
    outputfile.write("Demographic makeup of the group surveyed:\n")
    for subcat, perc in finallist:
        if subcat in categoryrefdic["Wage"]:
            outputfile.write("%4.1f percent of this group earns % %-20s \n" %perc %subcat)
        elif subcat in categoryrefdic["Age"]:
            outputfile.write("%4.1f percent of this group is aged % %-20s \n" %perc %subcat)
        else:
            outputfile.write("%4.1f percent of this group is % %-20s \n" %perc %subcat)
    outputfile.close()
    return "Success! You can find the saved file named %-5s in the same location as this program." %outputname


#--------------------------------
try:
    print("This program analyzes the answers from a demographic survey to investigate the diversity of the group.")
    inputname = input("Please enter the file name of the database to analyze:")
    inputname = inputname+".txt"
    inputfile = open(inputname, "r")

    firstline = inputfile.readline()
    categorieslist = firstline.split(",")
    categorieslist = list(map(str.strip, categorieslist))

    restofdata = makelistofdata(inputfile)
    categoryrefdic = sliceintolists(categorieslist, restofdata)

    percentdic = makedicofperc(restofdata)
    outputlist = list(percentdic.items())
    outputlist = sorted(outputlist, key=operator.itemgetter(1), reverse=True)

    inputfile.close()

    showresults(outputlist)

    outputfile = input("Would you like to save these results? If yes, please enter file name. If no, you may exit the program now.")
    outputfile = outputfile+".txt"
    writetofile(outputfile, outputlist)
except:
    print("Error! Please check the input file.")
