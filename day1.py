# -------------------------------------------- P1 --------------------------------------------
def find_dist(l1, l2):
    l1.sort()
    l2.sort()
    distance_between = 0

    # here i am assuming that both lists will be off same length
    for i in range(len(l1)):
        distance_between += abs(l1.pop(0) - l2.pop(0))
    return distance_between
# -------------------------------------------- P1 --------------------------------------------

# -------------------------------------------- P2 --------------------------------------------
def find_sim_score(l1, l2):
    '''
    sim_map = dict(zip(l1, [None]*len(l1)))
    for x,y in sim_map.items():
        if y is None:
            multiple = y.count(x)
            y = x * multiple
    '''
    sim_score = 0
    # once again assuming both lists are same length
    for i in range(len(l1)):
        sim_score += l1[i] * l2.count(l1[i])

    return sim_score
# -------------------------------------------- P2 --------------------------------------------

# ------------------------------------------ TEST/OUTPUT ------------------------------------------
# parsing input
l1, l2 = [], []
with open('d1_input.txt', 'r') as file:
    for line in file:
        left, right = line.split()
        l1.append(int(left))
        l2.append(int(right))

# Test Output for P1
#print(find_dist(l1=l1,l2=l2))

# Test Output for P2
print(find_sim_score(l1=l1, l2=l2))
# ------------------------------------------ TEST/OUTPUT ------------------------------------------