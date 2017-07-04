'''consecutive check'''
def check_consecutive(d):
    d
    if 14 in d:
        d.append(1)
    d.sort()
    strike = 0
    maxi = 0
    m = 0
    while m<len(d):
        newgroup = []
        newgroup.append(d[m])
        n=m+1
        while n<len(d):
            if d[n] in newgroup:
                n=n+1
            elif (d[n]-1) in newgroup:
                newgroup.append(d[n])
                n=n+1
            else:
                n=n+1
        if len(newgroup)>=5:
            strike = 1
            if max(newgroup)>maxi:
                 maxi = max(newgroup)
        m += 1
        
    return (strike,maxi)

'''duplicate checking'''
def check_duplicate(data):
    t =  list(set(data))
    double = [x for x in t if data.count(x)==2]
    triple = [x for x in t if data.count(x)==3]
    quadruple = [x for x in t if data.count(x)==4]
    fiveofakind = [x for x in t if data.count(x)==5]
    return (double,triple,quadruple,fiveofakind)

'''check type'''
def check_type(suit,data):
    newdata = []
    double,triple,quadruple,fiveofakind = check_duplicate(suit)
    if len(fiveofakind) == 1:
        kind = fiveofakind[0]
        k=0
        while k<7:
            if suit[k]==kind:
                newdata.append(data[k])
            k+=1
        if len(newdata)>4:
            flushstrike,maxflushstrike = check_consecutive(newdata)
    else:
        newdata=[0]
        flushstrike=0
        maxflushstrike=0
    return (len(fiveofakind),sorted(newdata,reverse=True),flushstrike,maxflushstrike)
'''biggest'''
def biggest(data,suit):
    flush,maxflush,flushstrike,maxflushstrike = check_type(suit,data)
    if flushstrike ==1:
        return(9*10000000000+maxflushstrike)
    else:
        double,triple,quadruple,temp = check_duplicate(data)
        if len(quadruple) == 1:
            return (8*10000000000+quadruple[0])
        elif len(triple)==2:
            return (7*10000000000+max(triple)*100+min(triple))
        elif len(triple)==1 and len(double)>=1:
            return (7*10000000000+triple[0]*100+max(double))
        elif flush == 1:
            return (6*10000000000+maxflush[0]*100000000+maxflush[1]*1000000+maxflush[2]*10000+maxflush[3]*100+maxflush[4])
        else:
            strike,maxstrike = check_consecutive(data)
            if strike == 1:
                return (5*10000000000+maxstrike)
            elif len(triple)==1:
                data.remove(triple[0])
                data.remove(triple[0])
                data.remove(triple[0])
                temp= sorted(data,reverse=True)
                return(4*10000000000+triple[0]*10000+temp[0]*100+temp[1])
            elif len(double)>=2:
                temp1 = sorted(double,reverse=True)
                data.remove(double[0])
                data.remove(double[0])
                data.remove(double[1])
                data.remove(double[1])
                temp2 = sorted(data,reverse=True)
                return(3*10000000000+temp1[0]*10000+temp1[1]*100+temp2[0])
            elif len(double)==1:
                data.remove(double[0])
                data.remove(double[0])
                temp3=sorted(data,reverse=True)
                return(2*10000000000+double[0]*1000000+temp3[0]*10000+temp3[1]*100+temp3[2])
            else:
                temp4 =  sorted(data,reverse=True)
                return(1*10000000000+temp4[0]*100000000+temp4[1]*1000000+temp4[2]*10000+temp4[3]*100+temp4[4])
            
'''compare'''
'''def compare(suit1,data1,suit2,data2):
    flush1,maxflush1,flushstrike1,maxflushstrike1 = check_type(suit1,data1)
    flush2,maxflush2,flushstrike2,maxflushstrike2 = check_type(suit2,data2)
    if flushstrike1>flushstrike2:
        return 1
    elif flushstrike2>flushstrike1:
        return 2
    elif flushstrike1==1 and flushstrike2==1:
        if maxflushstrike1 > maxflushstrike2:
            return 1
        elif maxflushstrike1 < maxflushstrike2:
            return 2
        elif maxflushstrike1 == maxflushstrike2:
            return 0
    elif flushstrike1==0 and flushstrike2==0:
        double1,triple1,quadruple1,temp1 = check_duplicate(data1)
        double2,triple2,quadruple2,temp2 = check_duplicate(data2)
        if len(quadruple1)>len(quadruple2):
            return 1
        elif len(quadruple1)<len(quadruple2):
            return 2
        elif len(quadruple1)==1 and len(quadruple2)==1:
            if quadruple1[0]>quadruple2[0]:
                return 1
            else:
                return 2
        elif len(quadruple1)==0 and len(quadruple2)==0:
            if (len(triple1)==1 and len(double1) ==1) and (len(triple2)==1 and len(double2)==1):
                if triple1[0]>triple2[0]:
                    return 1
                elif triple1[0]<triple2[0]:
                    return 2
                else:
                    if double1[0]>double2[0]:
                        return 1
                    elif double1[0]<double2[0]:
                        return 2
                    else:
                        return 0
            elif len(triple1)==1 and len(double1) ==1:
                return 1
            elif len(triple2)==1 and len(double2)==1:
                return 2
            else:'''
               

            
'''
data2 = [14,14,8,10,6,11,5]
suit2 = [1,2,3,4,3,4,2]
data1 = [13,5,10,13,6,2,7]
suit1 = [1,3,3,4,2,2,3]
largeness1 = biggest(data1,suit1)
largeness2 = biggest(data2,suit2)
print(largeness1,largeness2)
'''
'''
data = [8,9,10,13,6,7,13]
suit = [3,3,3,4,3,3,2]
flush,maxflush,flushstrike,maxflushstrike = check_type(suit,data)
print(flush,maxflush,flushstrike,maxflushstrike)
strike,maxstrike = check_consecutive(data)
print(strike,maxstrike)
double,triple,quadruple,temp = check_duplicate(data)
print (double,triple,quadruple)
'''

