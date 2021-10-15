def swap_last_item(List):
    s=len(List)
    #Bruh serves as a temporary variable to hold the first item in the list
    bruh=List[0]
    List[0]=List[s-1]
    List[s-1]=bruh
    return List

