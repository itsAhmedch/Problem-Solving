def prime_factors(n):
    if n > 0:
        i = 2
        p = {} 
        r=''
        while n != 1:
            if n % i == 0:
                if f'{i}' in p:
                    p[f'{i}'] += 1
                else:
                    p[f'{i}'] = 1
                n = n // i
            else:
                i += 1
                
        for number in p :
            print(number)
            print(p[number])
            if p[number] == 1 :
                r=r+f'({number})'
            else :
                r=r+f'({number}**{p[number]})'
        return r
   


def prime_factors2(n):
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
            
            
        
        
