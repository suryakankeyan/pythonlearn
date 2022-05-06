para=("hello how are you") #input
words=1 # words count start with 1 
for i in range(len(para)):# looping the para and count the number letters in para
    if (para[i]==" "): #this condition count number of space in para 
        words+=1
        '''
        hello" "how" "are" "you
        first" "=1+1=2
        second" "=2+1=3
        third" "=3+1=4
        '''
print(words) #so output is 4