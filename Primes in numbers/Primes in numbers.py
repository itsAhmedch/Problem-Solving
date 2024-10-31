def prime_factors(n):
    if n > 0 :
        i=2
        PrevI=i
        PrevN=n
        nb=0
        r=''
        while n != 1   :
            if(i != PrevI  ):
                if (PrevN%PrevI == 0) :
                    if (nb==1):
                        r=r+f'({PrevI})'
                    else:
                        r=r+f'({PrevI}**{nb})'
                
                nb=0
                PrevI=i
                PrevN=n
            
            if(n%i == 0):
                nb+=1
                print(i,n,n/i)
                n=n/i
            else:
                i+=1
                
            
        if (nb==1):
            r=r+f'({PrevI})'
        else:
            if(nb):
                r=r+f'({PrevI}**{nb})'
        return r
            
            
        
        
