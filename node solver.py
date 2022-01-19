import itertools
import math

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
]

# numSkills = int(input("Enter number of skills: "))
numSkills = 6
for i in range(9 - numSkills):
    letters.pop()

boostLevels = {}
for i in letters:
    # boostLevels[i] = int(input("Times to boost skill " + i + ": "))
    boostLevels[i] = 2

current_nodes = []
stopInput = 0
# while (stopInput == 0):
#     nodeStr = input("Enter node: ")
#     if (nodeStr == "stop"):
#         stopInput = 1
#     elif (len(nodeStr) == 3):
#         newNode = [nodeStr[0], nodeStr[1], nodeStr[2]]
#         current_nodes.append(newNode)
current_nodes = [['f', 'e', 'd'], ['c', 'b', 'f'], ['d', 'a', 'e'], ['a', 'b', 'c']]

count = [0]

def find_all_solutions(current_nodes, boostLevels, blacklist, nodes_taken,
                    sol):
    count[0] += 1
    if all(v <= 0 for v in boostLevels.values()):
        sol.append(nodes_taken)
        return nodes_taken
    elif all(v < 2 for v in boostLevels.values()) and (sum(boostLevels.values()) == 3):
        sol.append(nodes_taken)
    if len(current_nodes) == 0:
        return False

    node = current_nodes.pop()

    # we cannot take it
    if node[0] in blacklist or \
    node[0] not in boostLevels or node[1] not in boostLevels or node[2] not in boostLevels or  \
    boostLevels[node[0]] == 0 or boostLevels[node[1]]==0 or boostLevels[node[2]]==0:
        return find_all_solutions(current_nodes, boostLevels, blacklist,
                               nodes_taken, sol)
    else:
        # we can but don't take it
        donttake = find_all_solutions(current_nodes[:], boostLevels,
                                   blacklist[:], nodes_taken[:], sol)
        # we take it, update needs_dict
        dic = boostLevels.copy()
        for i in node:
            dic[i] = dic[i] - 1
        take = find_all_solutions(current_nodes[:], dic,
                               blacklist + [node[0]],
                               nodes_taken + [node], sol)

        return sol

# def check_a_solution(sol, boostLevels):
#     dic = boostLevels.copy()
#     for i in sol:
#         for j in i:
#             dic[j] -= 1
#     return all(v <= 0 for v in dic.values())

solutions = find_all_solutions(current_nodes, boostLevels, [], [], [])

# for i in solutions:
#     assert check_a_solution(i, boostLevels)

# remove dupes
solutions.sort()
solutions = list(solutions for solutions,_ in itertools.groupby(solutions))

def missingSkills(sol, boostLevels):
    dic = boostLevels.copy()
    skills = []
    for i in sol:
        for j in i:
            dic[j] -= 1
    for i in dic:
        if dic[i] == 1:
            skills.append(i)
    return skills

nodesNeeded = math.ceil(sum(boostLevels.values()) / 3)
print("Solutions:")
if any(len(i) == nodesNeeded for i in solutions):
    for i in solutions:
        if len(i) == nodesNeeded:
            print(i)
else:
    print("No solution. Searching for near solutions...")
    for i in solutions:
        print(i)
        missing = missingSkills(i, boostLevels)
        print("Missing skills: " + missing[0] + ", " + missing[1] + ", " + missing[2])