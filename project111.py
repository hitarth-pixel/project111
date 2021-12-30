import pandas as pd
import plotly.figure_factory as ff
import csv
import statistics as st
import random as r

df= pd.read_csv("data2.csv")
lists=df["claps"].tolist()
mean1=st.mean(lists)
std1=st.stdev(lists)
print("population mean of whole data is- "+str(mean1))
print("standard deviation of whole data is- "+str(std1))


def randomSetOfMean(counter):
    a1=[]
    for i in range(0,counter):
        a=r.randint(0,len(lists)-1)
        value=lists[a]
        a1.append(value)
    mean=st.mean(a1)
    return mean

def findMean(meanList):
    df=meanList
    mean=st.mean(df)
    fig=ff.create_distplot([df],["claps"],show_hist=False)
    #fig.add_trace(x=(mean,mean),y=())
    fig.show()

def setup():
    meanList=[]
    for i in range(0,100):
        a=randomSetOfMean(30)
        meanList.append(a)
    findMean(meanList)
    mean2=st.mean(meanList)
    print("mean of sample distribution is- "+str(mean2))
    return mean2
mean2=setup()
def standardDeviation():
    stdList=[]
    for i in range(0,100):
        a=randomSetOfMean(30)
        stdList.append(a)
    stddev=st.stdev(stdList)
    print("standard deviation of sample distribution is- "+str(stddev))
    return stddev
stddev=standardDeviation()

firstStdStart=mean1-std1
secondStdStart=mean1-(2*std1)
thirdStdStart=mean1-(3*std1)
firstStdEnd=mean1+std1
secondStdEnd=mean1+(2*std1)
thirdStdEnd=mean1+(3*std1)

stdOfClaps1=[result for result in lists if result>firstStdStart and result<firstStdEnd]
stdOfClaps2=[result for result in lists if result>secondStdStart and result<secondStdEnd]
stdOfClaps3=[result for result in lists if result>thirdStdStart and result<thirdStdEnd]

print("{}% is the standard deviation of the claps 1".format(len(stdOfClaps1)*100.0/len(lists)))
print("{}% is the standard deviation of the claps 2".format(len(stdOfClaps2)*100.0/len(lists)))
print("{}% is the standard deviation of the claps 3".format(len(stdOfClaps3)*100.0/len(lists)))

ZScore=(mean1-mean2)/std1
print("z score of the data="+str(ZScore))