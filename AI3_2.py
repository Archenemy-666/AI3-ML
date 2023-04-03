def generate_binary_strings(size):
    """
    Generate all possible 6-bit binary strings using a greedy approach.
    """
    result = []
    for i in range(2**size):
        binary = bin(i)[2:].zfill(size)
        result.append(binary)
    return result,len(result)

def inputStats():
    size = int(input("number of vaccine comp"))
    List = []    
    for i in range(size):
        name = input("enter name of organization: ")
        cost = int(input("cost quote: "))
        population = int(input("population it serves "))
        List.append([name,cost,population]) 
    return List,size

def optimalSearch(binary_strings,List,ListSize,size):
    print("------------------------\n")
    print(binary_strings)
    print("------------------------\n")

    bestList = []
    for i in range (0,ListSize):
        total = 0
        tempOfList = []
        for j in range (0,size):
            if binary_strings[i][j] == '1':
                tempVal = List[j]
                print("tempVal : ",tempVal)
                total = tempVal[1] + total
                print("total: ",total)
                if total <= 100:
                    tempOfList.append(tempVal)
                    print("tempOfList : ",tempOfList)
                else:
                    total = total - tempVal[1]
                    print("list and total",tempOfList,total)
                
            else:
                continue
            print("\n")
            if tempOfList not in bestList:
                bestList.append(tempOfList)
            else:
                continue
    print("--------------")
    print("\n")
    print("bestList: ", bestList)

def main():
    List, size = inputStats()    
    binary_strings,ListSize = generate_binary_strings(size)
    optimalSearch(binary_strings,List,ListSize,size)

if __name__ == "__main__":
    main()
