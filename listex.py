#li=[2,5,6,8,5,8]
#li.append(56)
#li.insert(0,98)
#li[0]=52
#print(li[4][1])
#x=li.pop(4)
#x=li.remove(5)
#del li[0:3]
#x=0
'''for i in range(0,len(li),1):
    x=x+li[i]#x=0+2#x=2+5#x=7+6#x=13+8

for i  in li:
    x=x+i
print(x)
'''
#li.sort()
#li.sort(reverse=True)
#li2=sorted(li)
#print(li2)
#print(li)
#print(li.count(5))

#li3=[[3,2],[3,1],[9,8]]

#li3.sort()

import re
li=['raj25.jpg','sip15.txt']

x=[]
def fetchData(lv):
    return float(re.findall(r"\d+",lv)[0])
for i in li:
    x.append(fetchData(i))


li.sort(key=fetchData)
print(li)









