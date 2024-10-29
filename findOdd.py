def find_it(seq):
    seq2=[]
    
    for i in range(0,len(seq)) :
        nb=0
        if  not (seq[i] in  seq2) :
            for j in seq :
                if j == seq[i] :
                    nb+=1
            if nb % 2 != 0 :
                return seq[i]
            seq2.append(seq)
                    
            
                
