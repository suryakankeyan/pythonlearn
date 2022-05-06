s=("hi this is surya") #input
c={} #c is dict to take keys and value in s (ex h=0,i=1 ...)
for i in s: #looping the s in i
    if i !=" ": #this condition make spaces is False 
       if i in c: #this condition  are take i in c
             c[i]=c[i]+1 
             """
             [] list cannot consider same value 
             c[h]=0+1=1
             c[i]=0+1=1
             c[t]=0+1=1
             c[h]=1+1=2
             c[i]=1+1=2
             c[s]=0+1=1
             c[i]=2+1=3
             c[s]=1+1=2
             c[s]=2+1=3
             c[u]=0+1=1
             c[r]=0+1=1
             c[y]=0+1=1
             c[a]=0+1=1          
             
             """
       else:
             c[i]=1 #this is starting value of c[i]
                                         # 1   2   3   4   5   6   7   8 ==output 
print(c) #c calculate the values of i ex h:2 i:3 t:1 s:3 u:1 r:1 y:1 a:1
print(len(c)) # but i count the length of c