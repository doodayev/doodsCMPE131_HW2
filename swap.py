def swap_last_item(List):
    s=len(List)
    bruh=List[0]
    List[0]=List[s-1]
    List[s-1]=bruh
    return List

