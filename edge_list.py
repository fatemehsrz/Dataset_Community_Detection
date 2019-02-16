
f= open('./citeseer/citeseer.cites', 'r')
 
list_name=[]
tuples=[]

for line in f:
    
    a= line.strip('\n').split('\t')
    
    print(a[0], a[1])   
    list_name.append(a[0])   
    list_name.append(a[1]) 
    tuples.append((a[0],a[1]))    
         
word2index = {}

for vo in list(set(list_name)):
    if word2index.get(vo) is None:
        word2index[vo] = len(word2index)
  
index2word = {v:k for k, v in word2index.items()} 
     
f_e= open('citeseer.edgelist', 'w')          
 
e_count=0  
 
for u,v in tuples:
     
    f_e.write(str(word2index[u])+' '+ str( word2index[v]))  
    f_e.write('\n')   
     
    e_count+=1
              
f_e.close()

print( e_count)



f= open('./citeseer/citeseer.content', 'r')

f_l= open('citeseer.labels', 'w')  
 
list_name=[]
tuples=[]

for line in f:
    
    a= line.strip('\n').split('\t')
    
    print(word2index[a[0]],a[-1]) 
    
    f_l.write(str( word2index[a[0]])+' '+ str(a[-1] )) 
        
    
    for i in a[1:-1]:
        f_l.write(' '+i)
            
    f_l.write('\n')   
     
              
f_l.close()     
    











