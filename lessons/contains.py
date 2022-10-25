"""An example of a list utility algorithm"""
#function with 2 parameters
# needle : what we're searching for
# haystack: list of values we are searching in 
# return type: boolean
# start from first index
#loop throuhgh each index of list
#test if equal to needle
#yes: return true
#return false


def contains(needle: str, haystack: list[str]) -> bool():
    i = 0
    while i < len(haystack):
        if haystack[i] is needle:
            return True
            
        i += 1
    return False
    