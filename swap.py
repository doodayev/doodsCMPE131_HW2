def swap_last_item(List):
    s=len(List)
    bruh=List[0]
    List[0]=List[s-1]
    List[s-1]=bruh
    return List
 
# Driver function
TheList=[]
L=int(input("Enter number of elements: "))
for i in range(0, L):
    Thing=int(input())
    TheList.append(Thing)
print(TheList)
print(swap_last_item(TheList))
