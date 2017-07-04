from random import sample
import largeness
import statistics
def start(data1,data2):
     player1 = [data1,data2]
     player2 = []
     common = []
     lst = sample(range(0,49),7)
     lib = [21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124,131,132,133,134,141,142,143,144]
     lib.remove(data1)
     lib.remove(data2)
     player2 = [lib[lst[0]],lib[lst[1]]]
     common = [lib[lst[2]],lib[lst[3]],lib[lst[4]],lib[lst[5]],lib[lst[6]]]
     a = player1+common
     b = player2+common
     if convert(a)>convert(b):
         return 1
     elif convert(a)==convert(b):
         return 0.5
     else:
         return 0

def flop(data1,data2,data3,data4,data5):
     player1 = [data1,data2]
     player2 = []
     common = []
     lst = sample(range(0,46),4)
     lib = [21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124,131,132,133,134,141,142,143,144]
     lib.remove(data1)
     lib.remove(data2)
     lib.remove(data3)
     lib.remove(data4)
     lib.remove(data5)
     player2 = [lib[lst[0]],lib[lst[1]]]
     common = [data3,data4,data5,lib[lst[2]],lib[lst[3]]]
     a = player1+common
     b = player2+common
     if convert(a)>convert(b):
         return 1
     elif convert(a)==convert(b):
         return 0.5
     else:
         return 0
def turn(data1,data2,data3,data4,data5,data6):
     player1 = [data1,data2]
     player2 = []
     common = []
     lst = sample(range(0,45),3)
     lib = [21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124,131,132,133,134,141,142,143,144]
     lib.remove(data1)
     lib.remove(data2)
     lib.remove(data3)
     lib.remove(data4)
     lib.remove(data5)
     lib.remove(data6)
     player2 = [lib[lst[0]],lib[lst[1]]]
     common = [data3,data4,data5,data6,lib[lst[3]]]
     a = player1+common
     b = player2+common
     if convert(a)>convert(b):
         return 1
     elif convert(a)==convert(b):
         return 0.5
     else:
         return 0
def river(data1,data2,data3,data4,data5,data6,data7):
     player1 = [data1,data2]
     player2 = []
     common = []
     lst = sample(range(0,44),2)
     lib = [21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124,131,132,133,134,141,142,143,144]
     lib.remove(data1)
     lib.remove(data2)
     lib.remove(data3)
     lib.remove(data4)
     lib.remove(data5)
     lib.remove(data6)
     lib.remove(data7)
     player2 = [lib[lst[0]],lib[lst[1]]]
     common = [data3,data4,data5,data6,data7]
     a = player1+common
     b = player2+common
     if convert(a)>convert(b):
         return 1
     elif convert(a)==convert(b):
         return 0.5
     else:
         return 0
def convert(comb):
    data = [x//10 for x in comb]
    suit = [x % 10 for x in comb]
    return largeness.biggest(data,suit)
def ratecal(arg):
     a=len(arg)
     ave = []
     temp = []
     m=0
     while m<1000:
        n=0
        while n<100:
           if a ==2:
             t = start(arg[0],arg[1])
           elif a ==5:
             t= flop(arg[0],arg[1],arg[2],arg[3],arg[4])
           elif a == 6:
             t = turn(arg[0],arg[1],arg[2],arg[3],arg[4],arg[5])
           elif a == 7:
             t = river(arg[0],arg[1],arg[2],arg[3],arg[4],arg[5],arg[6])
           n+=1     
           temp.append(t)
        m+=1
        ave.append(statistics.mean(temp))
     return (statistics.mean(ave),statistics.stdev(ave))
             
print(ratecal([21,22]))
