# Tower of Hanoi
Towers = ["A","B","C"]
# Original state: A has n plates. B has 0 and C has 0.

def move(n,source,target):
    #move n plates from source to target
    if n == 1:
        print("Move 1 plate from source to target.")
    if n > 1:
        move(n-1,source,target)
        move(1,source,target)
        move(n-1,source,target)
        # source and target are changing. 
