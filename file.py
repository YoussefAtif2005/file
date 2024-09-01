
    

import os 
f=open('File.txt', 'r')
print(f.readlines())
try :
     n=int(input('Number of lines: '))
     with open('File.txt') as input_file:
           head = [next(input_file) for _ in range(n)]
           print(head)
except TypeError:
    print('Please enter an integer:') 

 
file = open('File.txt','r') 
lines = file.readlines() 
last_lines = lines[-5:] 
for line in last_lines: 
	print(line) 
file.close()     
    
with open('File.txt', 'r') as f:
    content=f.read()
    words=content.split(' ')
    numb_words=len(words)
    
print(f'Number of words: {numb_words}')    