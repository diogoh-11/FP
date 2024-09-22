
def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
        }


    print("a) Table of common interests:")
    commoninterests = {
        (p1, p2): interests[p1] & interests[p2]  
        for p1 in interests
        for p2 in interests
        if p1 < p2}
    print(commoninterests)

    print("b) Maximum number of common interests:")
    maxCI = max(len(commoninterests[p,q]) for p,q in commoninterests)
    print(maxCI)

    print("c) Pairs with maximum number of matching interests:")
    maxmatches = [pair for pair, num in commoninterests.items() if len(num) == maxCI]
    print(maxmatches)

    print("d) Pairs with low similarity:")
    lowJaccard = [pair for pair, num in commoninterests.items() if len(num)/len(interests[pair[0]] | interests[pair[1]]) < 0.25]
    print(lowJaccard)


# Start program:
main()

