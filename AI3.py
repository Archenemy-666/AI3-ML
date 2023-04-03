#read dataset
#choose the Greedy Search to find the best allocation of 100 Million from the list to reach  most people
#Use Genetic Algorithm for optimization of the best options that increase the number of people vaccinated within 100 Million

def inputStats():
    ListSize = int(input("number of vaccine comp"))
    List = []    
    for i in range(ListSize):
        name = input("enter name of organization: ")
        cost = int(input("cost quote: "))
        population = int(input("population it serves "))
        List.append([name,cost,population]) 
    return List
def greedySearch():
    List = inputStats()
    from operator import itemgetter
    List = sorted(List, key=itemgetter(2), reverse = True)
    ListIndex = List
    tempList = []
    total = 0
    #apply dfs on the list to perform greedy search
    while ListIndex:
        pointer = ListIndex.pop()
        pointerValue = pointer[1]  
        while List:
            length = len(List)
            count = 0
            nextP = (List.pop())
            nextPvalue = nextP[1]
            #swapping if we are not dealing with the same initial value
            if count == 0 and (pointerValue != nextPvalue):
                for i in List:
                    token = 0
                    if i == pointer:
                        List[i],List[length-1] = List[length-1],List[i]
            print("the swapped list : ",List)
            total = nextPvalue + total
            if total > 100:
                continue
            else :
                tempList.append(nextP) 
            print("total: ",total)
            count = count + 1

    return List

def main():
    x = greedySearch()
    print(x)

if __name__ == "__main__":
    main()

 
