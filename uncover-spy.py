# coding challenge problem for unit assessment
# from CodeSignal

# prompt: in a city-state of n people, there is a rumor going
# around that one of the n people is a spy for the neighboring
# city state. The spy, if it exits:
# 1. does not trust anyone
# 2. is trusted by everyone else
# 3. works alone ( not other spies)

# You are given a list of pairs, gtus. Each trust[i] = [a,b]
# represent the fact that the person a trusts person b.
# if the spy exists and can be found, return their identifier.
# otherwise return -1


#inputs:
    #n = population of city, integer
    #trust = list of pairs [a,b], meaning person a trusts person b

#output:
    #integer, the spy of the city

#notes:
#the spy does not trust anyone, so cannot be in the position a
#spy is trusted by everyone, so must be in the position b
#set two pointers:
    #truster = person giving trust
    #trustee = person receiving trust


# trustee: of vertex (person) is # of directed edges going towards it. how many people trust person, receiving trust
# truster: of vertex (person) is # of directed edges going into it. # people trusted by that person, giving trust
# spy: outdgree of 0 and truster of n-1 (everyone trusts them except the spy)
# return: identifier if spy found, else -1

#Example:
#Input: n = 3, trust = [[1, 3], [2, 3]]
#Output: 3
#Explanation: Person 1 trusts Person 3. Person 2 trusts Person 3. But Person 3 does NOT trust Person 1 or 2. So, Person 3 must be the spy.

def uncover_spy(n, trust):
    if len(trust) < n-1:
        return -1

    truster = [0] * (n + 1)
    trustee = [0] * (n + 1)

    for x, y in trust:
        trustee[x] += 1
        truster[y] += 1

    for i in range(1, n + 1):
        if truster[i] == n - 1 and trustee[i] == 0:
            return i
    return -1