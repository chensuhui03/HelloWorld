#Tower of Hanoi through index
Towers = ["A","B","C"]

def print_ops(n,source_index,target_index):
    source = Towers[source_index]
    target = Towers[target_index]
    print("Move {}th plate from {} to {}".format(n,source,target))

def Move(n,source_index,target_index):
    #Ending condition
    if n == 1:
        print_ops(n,source_index, target_index)
        return
    #solving subproblem: move n-1 plate from source to new target
    new_target_index = cal_new_target_index(source_index,target_index)
    Move(n-1,source_index,new_target_index)
    #solve current problem:move nth plate from source to target, move n-1 plates
    # from new target to target
    print_ops(n,source_index,target_index)
    Move(n-1,new_target_index,target_index)
    
def cal_new_target_index(source_index,target_index):
    new_target_index = 3 - source_index - target_index
    return new_target_index

Move(5,0,1)