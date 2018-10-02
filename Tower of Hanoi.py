# Tower of Hanoi
Towers = ["A","B","C"]
# Original state: A has n plates. B has 0 and C has 0.

# source = 0 or 2. When is source 0?

def move_action(n, source, target):
    # can be print
    print_vars(n, source,target)
    # can be showing animation

def move(n,source,target):
    #part1: ending condition when there is only 1 plate left 
    # to move from source to target
    if n == 1:
        move_action(n, source, target)
        return
    #part2: solve subproblem move n-1 from source to new target
    new_target = cal_new_target(source,target)
    move(n-1,source,new_target)

    #part3: handle current: move nth plate from source to target 
    # and move n-1 plate from new target to target.
    #move(1,source,target)
    move_action(n, source, target)
    move(n-1,new_target,target)
    
    

def print_vars(n, source,target):
    print("Move {}th plate from {} to {}".format(n, source,target))

def cal_new_target(source,target):
    source_index = Towers.index(source)
    target_index = Towers.index(target)
    new_target_index = 3 - source_index - target_index
    new_target = Towers[new_target_index]
    return new_target

#move(3, "A", "B")

try:
    idx = Towers.index(1)
except:
    print("1 is not in Towers")



