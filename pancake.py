import random

class Pancake:
    def __init__(self, idx, up_down):
        self._idx = idx
        self._up_down = up_down

    def print(self):
        print("Pancake #{} is burning side {}".format(self._idx, self._up_down))

    def flip_status(self):
        if self._up_down == up_str:
            self._up_down = down_str
        else:
            self._up_down = up_str

    def is_up(self):
        return self._up_down == up_str
    
    def is_down(self):
        return self._up_down == down_str

up_str = "UP"
down_str = "DOWN"

p1 = Pancake(0, up_str)
#p1.print()

class Pancake_Stack:
    def __init__(self):
        self._pancakes = []

    def add_pancake(self, p):
        self._pancakes.append(p)

    def print(self):
        print("Pancake Stack has the following pancakes:")
        for i in reversed(self._pancakes):
            i.print()

    def flip(self, i):
        if (i >= len(self._pancakes)):
            return 

        print("Now flipping from index: ", i)
        tmp = self._pancakes[i:]
        tmp.reverse()
        self._pancakes[i:] = tmp

        for i in self._pancakes[i:]:
            i.flip_status()
        self.print()

    def suhui_algo(self):
        n = len(self._pancakes)
        i = n - 1
        while i > 0:
            if self._pancakes[i]._up_down == self._pancakes[i-1]._up_down:
                i = i - 1
            else:
                self.flip(i)
        if self._pancakes[0]._up_down == up_str:
            self.flip(0)

    def tianheng_algo(self,i):
        #print("calling i = ", i)

        n = len(self._pancakes)
        if i == n-1 and self._pancakes[i]._up_down == up_str:
            self.flip(i)
            return
        elif i == n-1 and self._pancakes[i]._up_down == down_str:
            return
        
        self.tianheng_algo(i+1)

        if self._pancakes[i]._up_down == down_str:
            return
        else:
            self.flip(i+1)
            self.flip(i)    

    def tianheng_algo_opt(self, i, all_up):
        n = len(self._pancakes)
        # Part1. termination conditions
        if (i == n-1):
            if (all_up):
                if (self._pancakes[i].is_down()):
                    self.flip(i)
            else:
                if (self._pancakes[i].is_up()):
                    self.flip(i)
            return  

        # Part2. recusion and subproblem
        sub_all_up = False
        if (self._pancakes[i].is_up()):
            sub_all_up = True   
        self.tianheng_algo_opt(i+1, sub_all_up)
        

        # Part3. action based on subproblem results
        if (all_up):
            if (sub_all_up):
                return
            else:
                self.flip(i)
        else:
            if (sub_all_up):
                self.flip(i)
            else:
                return
        

    
        
    def making_all_down(self):
        #self.tianheng_algo(0)
        self.tianheng_algo_opt(0, False)
        


pancakes = Pancake_Stack()
number_of_pancakes = 5
for i in range(0, number_of_pancakes):
    seed = random.randint(0, 1)
    if (seed == 1):
        p = Pancake(i, up_str)
    else:
        p = Pancake(i, down_str)
    pancakes.add_pancake(p)

#pancakes.print()
#pancakes.making_all_down()

p0 = Pancake(0, up_str)
p1 = Pancake(1, up_str)
p2 = Pancake(2, up_str)
p3 = Pancake(3, down_str)
p4 = Pancake(4, up_str)
pcks = Pancake_Stack()
pcks.add_pancake(p0)
pcks.add_pancake(p1)
pcks.add_pancake(p2)
pcks.add_pancake(p3)
pcks.add_pancake(p4)
pcks.print()
pcks.making_all_down()
#pcks.print()






