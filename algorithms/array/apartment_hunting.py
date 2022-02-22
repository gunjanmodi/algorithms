"""
Apartment Hunting

  You're looking to move into a new apartment, and you're given a list of blocks
  where each block contains an apartment that you could move into. In order to
  pick your apartment, you want to optimize its location. You also have a list
  of requirements: a list of buildings that are important to you. For instance,
  you might value having a school and a gym near your apartment. The list of
  blocks that you have contains information at every block about all of the
  buildings that are present and absent at the block in question. For instance,
  for every block, you might know whether a school, a pool, an office, and a gym
  are present.

Sample Input:

blocks  = [
  {
    "gym": false,
    "school": true,
    "store": false,
  },
  {
    "gym": true,
    "school": false,
    "store": false,
  },
  {
    "gym": true,
    "school": true,
    "store": false,
  },
  {
    "gym": false,
    "school": true,
    "store": false,
  },
  {
    "gym": false,
    "school": true,
    "store": true,
  },
]

reqs =  ["gym", "school", "store"]

Sample Output:
3  // at index 3, the farthest you'd have to walk to reach a gym, a school, or a store is 1 block; at any other index, you'd have to walk farther
"""


"""
Solution 1
"""
def apartment_hunting1(blocks, reqs):
    max_distance_for_blocks = [float('-inf') for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closest_req_distance = float('inf')
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closest_req_distance = min(closest_req_distance, distance_between(i, j))
            max_distance_for_blocks[i] = max(max_distance_for_blocks[i], closest_req_distance)
    return min_distance_at_index(max_distance_for_blocks)

def min_distance_at_index(array):
    min_value = float('inf')
    min_value_index = 0
    for i in range(len(array)):
        current = array[i]
        if current < min_value:
            min_value = current
            min_value_index = i
    return min_value_index

def distance_between(a, b):
    return abs(a - b)      


"""
Solution 2
"""
def apartment_hunting(blocks, reqs):
    # min_distance_from_blocks = list(map(lambda req: get_min_distance(blocks, req), reqs))
    min_distance_from_blocks = []
    for req in reqs:
        min_distance_from_blocks.append(get_min_distance(blocks, req))
    max_distance_at_blocks = get_max_distance_at_blocks(blocks, min_distance_from_blocks)
    return min_distance_at_index(max_distance_at_blocks)

def get_max_distance_at_blocks(blocks, min_distance_from_blocks):
    max_distance_at_blocks = [0 for block in blocks]
    for i in range(len(blocks)):
        min_distance_at_block = list(map(lambda distances: distances[i], min_distance_from_blocks))
        max_distance_at_blocks[i] = max(min_distance_at_block)
    return max_distance_at_blocks

def get_min_distance(blocks,req):
    min_distances = [0 for block in blocks]
    closest_req_index = float('inf')
    for i in range(len(blocks)):
        current = blocks[i]
        if current[req]:
            closest_req_index = i
        min_distances[i] = distance_between(i, closest_req_index)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closest_req_index = i
        min_distances[i] = min(min_distances[i], distance_between(i, closest_req_index))
    return min_distances




    
if __name__ == '__main__':
    blocks = [
        {"gym": False, "school": True, "store": False},
        {"gym": True, "school": False, "store": False},
        {"gym": True, "school": True, "store": False},
        {"gym": False, "school": True, "store": False},
        {"gym": False, "school": True, "store": True}
    ]
    reqs = ["gym", "school", "store"]
    print(apartment_hunting(blocks, reqs))