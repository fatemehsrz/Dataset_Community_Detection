
f= open('./citeseer-origin/citeseer.cites', 'r')
 
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
     

f= open('./citeseer-origin/citeseer.content', 'r')

labels=[]
for line in f:
    
    a= line.strip('\n').split('\t')
    
    print(a[-1]) 
    
    labels.append(a[-1])
     
              
  
label2index = {}

for vo in list(set(labels)):
    if label2index.get(vo) is None:
        label2index[vo] = len(label2index)
  



f= open('./citeseer-origin/citeseer.content', 'r')

f_l= open('./citeseer-processed/citeseer.labels', 'w')
  
f_vec= open('./citeseer-processed/citeseer.vectors', 'w') 

node_list=[]

for line in f:
    
    a= line.strip('\n').split('\t')
    
    print(word2index[a[0]],a[-1], label2index[a[-1]]) 
    
    f_l.write(str( word2index[a[0]])+' '+ str(label2index[a[-1]] ) ) 
    f_l.write('\n') 
        
    node_list.append(word2index[a[0]])   
    
    f_vec.write(str( word2index[a[0]]))
    
    for i in a[1:-1]:
        f_vec.write(' '+i)
            
    f_vec.write('\n')   
     
              
f_l.close()
f_vec.close()


f_e= open('./citeseer-processed/citeseer.edgelist', 'w')          
 
e_count=0  
 
for u,v in tuples:
    
    if word2index[u] in node_list and word2index[v] in node_list:
     
       f_e.write(str(word2index[u])+' '+ str( word2index[v]))  
       f_e.write('\n')   
     
       e_count+=1
              
f_e.close()

print( e_count)
