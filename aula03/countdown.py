import time
def num():
    N=int(input("Qual é o número: "))
    print(N)
    time.sleep(1)
    return N

def countdown(N):
    if N > 0:
        print(N-1)
        time.sleep(1)
        N -= 1 
        countdown(N)
    else:
        print("Finish")
N = num()
countdown(N)

        
    

    
    
