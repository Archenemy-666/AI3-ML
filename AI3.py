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
    return List



def main():
    x = greedySearch()
    print(x)

if __name__ == "__main__":
    main()

 
