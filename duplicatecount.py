para=("hello you win i win") #input
words=para.split(" ") #to split the para
count={} # count is dict to take keys and value
for i in words: #looping the i in words
    if i !=" ": #this condition take space false
        if i in count: #this condition take i in count
            count[i]+=1
            '''
            count[hello]=0+1=1
            count[you]=0+1=1
            count[win]=0+1=1
            count[i]=0+1=1
            count[win]=1+1=2
            '''
        else:
            count[i]=1    #    1     2     3   4 
print(count)              #hello:1 You:1 win:2 i:1
print(len(count)) #output is 4
