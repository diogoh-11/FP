# Given a string s and a string t, return a string in which all the characters 
# of s that occur in t have been replaced by a _ sign. The comparisons are 
# case sensitive.


def replaceCharactersWithUnderscores(s, t):
    new = ""
    for l in s:
        if l in t:
           new += "_"
        else:
           new += l
    return new

        
        