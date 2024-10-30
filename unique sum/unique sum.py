def unique_sum(lst):
    l2=[]
    nb=0
    for i in lst :
        if not(i in l2):
            nb+=i
            l2.append(i)
    if(not(nb)):
        return None
    
    return nb
   
