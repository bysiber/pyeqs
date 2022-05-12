import random
import math

OPERATORS= ["*","+","-","**","/"]
CHRS = ["a","b","c","d","e","f","g"]
CONS = [-1,1,math.pi,math.e]
class eqGen():
    def __init__(self,vars,weightNum=0,opsMode="normal"):
        self.vars = vars
        self.weights = []
        self.maxWeightNum = 6
        self.maxVarNum = 3
        self.ops = []
        self.wOps = []
        self.eqList = []
        self.opsMode = opsMode
        self.weightNum = weightNum 
        self.lenVars = 0
        if self.weightNum != "random":
            self.weights = CHRS[0:self.weightNum]

        self.setWeights()
        self.setOps(set=True)
    
    def printInfos(self,showEqs=False):
        print("-VARS-\n",self.vars)
        print("-OPS-\n",self.ops)
        print("OPS-MODE: ",self.opsMode)
        print("Extra-Vars Num: ",self.weightNum)
        print("________________")
        if showEqs == True:
            self.printEqs()

    def setVars(self,sVars):
        vars = []
        for i in range(len(sVars)):
            for j in range(random.randint(1,self.maxVarNum)):
                vars.append(sVars[i])
        self.lenVars = len(vars) + len(self.weights)
        return vars


    def setWeights(self):
        if self.weightNum == "random":
            self.weights = CHRS[0:random.randint(1,self.maxWeightNum)]
        
    def setOps(self,set=False):
        if set == True:
            self.wOps = []
            #add extra operator,normal or random, if .(num)(op) in string opsMode
            #add 12 times * to Wops, example -> random.12*, or example -> normal.12*

            #copy OPERATORS to self.ops, example: if len = 5 -> ["*","+","-","*","+"]
            if "." in self.opsMode:
                    self.wOps += [self.opsMode[-1::] for _i in range(int(self.opsMode[7:len(self.opsMode)-1]))]

            self.wOps += OPERATORS
        else:
            if "normal" in self.opsMode:
                self.ops = [self.wOps[i%len(self.wOps)] for i in range(self.lenVars-1)]
            # this will be random index and random amount of per operator
            elif "random" in self.opsMode:
                self.ops = [random.choice(self.wOps) for i in range(self.lenVars-1)]

    def clearList(self):
        self.eqList = []

    def getEqs(self):
        return self.eqList
    
    def printEqs(self):
        print("@---> EQ LIST <---@")
        for i in range(len(self.eqList)):
            print(f"{i}.EQ: {self.eqList[i]}")
            

    def getChangedVarSigns(self):
        vars = []
        for i in range(len(self.vars)):
            if random.randint(0,1):
                vars.append("+" + self.vars[i])
            else:
                vars.append("-" + self.vars[i])
        return vars


    def eqGenerator(self,eqNum,changeOps=True,changeOpPos=True):
        self.clearList()
        for _eq in range(eqNum):
            bp = False
            unum = False
            strGen = ""
            counter = 0
            self.setWeights()
            nums = self.setVars(self.getChangedVarSigns()) + self.weights
            if changeOps == True or self.weightNum == "random":
                self.setOps()

            ops = self.ops
            
            if changeOpPos == True:
                random.shuffle(ops)
            random.shuffle(nums)

            while not nums == []:
                if bp == False:
                    if counter % 2==0:
                        if random.randint(0,100) > 49:
                            strGen+="("
                            bp=True
                            par = counter
                else:
                    if counter != 1 and counter %2 ==1 and (counter-par) > 2:
                        if random.randint(0,100) > 49:
                            strGen+=")"
                            bp = False

                if unum == False:
                    #strGen += random.choice(["+","-"]) + nums[0]
                    strGen += nums[0]
                    unum = True
                    nums = nums[1:]
                else:
                    strGen += ops[0]
                    ops = ops[1:]
                    unum=False
        
                counter+=1

            if bp == True:
                strGen+=")"
            self.eqList.append(strGen)


def generateRandomNumList(length,ext,mode=0):
    if mode == "random": # random select mode
        mode = random.randint(0,3)
    if mode == 0: # just number
        return [random.randint(-ext,ext)/random.randint(1,ext) or 1 for _i in range(length)]
    elif mode == 1: # %50 number and %50 (1,e,pi...)
        if random.randint(0,1):
            rlist = [random.randint(-ext,ext)/random.randint(1,ext) or 1 for _i in range(length)]
        else:
            rlist = [random.choice(CONS) for _i in range(length)]
        return rlist
    elif mode == 2: # (rand.num + 0,1,e,pi,...)
        return [random.choice(CONS+[random.randint(-ext,ext)/random.randint(1,ext) or 1]) for _i in range(length)]
    elif mode == 3: # just (0,1,e,pi,...)
        return [random.choice(CONS) for _i in range(length)]
    

#these elements are bits for trying to find XOR string eqs 
elements1 =   [1,0,1,0] # bits1
elements2 =   [1,0,0,1] # bits2
bitsNum = len(elements1)
result =   [0,0,1,1] # bits resulting in xor function(XOR)
best_error = 9999999 # initial value with max error
weightVars = ['a','b','c','d','e','f'] # (weight) multiplier veriables

if __name__ == "__main__":
    # if eqGen -> self.weightNum if it's "random", it will randomize the number of given variable arguments. like "x" , 3 times or 10 times
    # if weightNum -> second random argument -> if it's random it's length will be random between 0 and 6
    eqC = eqGen(["x","y"],"random","random") # -> how much input do you have ? for this -> there are two input -> 'x' and 'y'
    eqNum = 5000 # how many equations will be generated
    eqC.eqGenerator(eqNum) # generating function
    eqs = eqC.getEqs() # get all the equations
    #eqC.printInfos()
    for i in range(eqNum):
        error = 0 # error variable to be used for each equation
        #if eqC's weightNum parameter-> we set it to "random". t
        weights = generateRandomNumList(eqC.maxWeightNum,1000,1) # how many random (weight) multiplier values ​​do you want, its len(eqC.weights) because we set the second argument to "random"
        for var,weight in zip(weightVars[:eqC.maxWeightNum-1],weights):
            exec(var+" = "+str(weight))
        for j in range(bitsNum):
            x = elements1[j]
            y = elements2[j]
            try:
                out=eval(eqs[i])
                error += abs(result[j] - out)
            except:
                #except_counter +=1
                error = 99999999


        if error < best_error:
            best_error = error
            best_eq = eqs[i]
            best_weights = weights
        if error == 0:
            break
print("---------------------------")
print(f"BEST EQ: {best_eq}  ---> ERROR: %{(best_error / sum(result)*100)}")
print("---------------------------")
print(f"Your inputs -> {eqC.vars}")
for var,weight in zip(weightVars,best_weights):
    print(var+" = "+str(weight))