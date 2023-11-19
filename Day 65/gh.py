def binary_search(arr,start,end,key):
    if end >= start:
        mid = (end + start) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr,mid+1,end,key)
        else: 
            return binary_search(arr,start,mid-1,key)
            
    else:
        return -1
    
x = "hello"



"""
 Answer of Climbing the Leaderboard question in hacker rank
def binary_search(arr,start,end,key):
    if end >= start:
        mid = start+(end - start) // 2
        if arr[mid] == key:
            return mid+1
        elif arr[mid] > key:
            if mid+1 != len(arr) and arr[mid+1] < key:
                return mid +2
            
            return binary_search(arr,mid+1,end,key)
            
        
        else: 
            return binary_search(arr,start,mid-1,key)
            
    else:
        if key >= arr[end]:
            return start+1
        elif start > end:
            return len(arr)+1
        
        

def climbingLeaderboard(ranked, player):
    
    ranks = []
    var_ = ranked[0]
    ranks.append(var_)
    for x in ranked:
        if x != var_:
            ranks.append(x)
            var_ = x

    places = []
    for score in player:
        res = binary_search(ranks,0,len(ranks)-1,score)
        places.append(res)
    
    
    
    return places
        
"""