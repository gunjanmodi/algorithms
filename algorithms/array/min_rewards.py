import unittest

# O(n^2) time | O(n) space
# def min_rewards(scores):
#     rewards = [1 for _ in scores]
#     for i in range(len(scores)):
#         j = i - 1
#         if scores[i] > scores[j]:
#             rewards[i] = rewards[j] + 1
#         else:
#             while j >= 0 and scores[j] > scores[j + 1]:
#                 rewards[j] = max(rewards[j], rewards[j + 1] + 1)
#                 j -= 1
#     return sum(rewards)

# O(n) time | O(n) space
def min_rewards(scores):
    rewards = [1 for _ in scores]
    local_min_idxs = get_local_min_idxs(scores)
    for local_min_idx in local_min_idxs:
        expand_local_min_idx(local_min_idx, scores, rewards)
    return sum(rewards)

def expand_local_min_idx(local_min_idx, scores, rewards):
    left_idx = local_min_idx - 1
    while left_idx >= 0 and scores[left_idx] > scores[left_idx + 1]:
        rewards[left_idx] = max(rewards[left_idx], rewards[left_idx + 1] + 1)
        left_idx -= 1
    right_idx = local_min_idx + 1
    while right_idx < len(scores) and scores[right_idx] > scores[right_idx - 1]:
        rewards[right_idx] = rewards[right_idx - 1] + 1
        right_idx += 1
        
def get_local_min_idxs(array):
    if len(array) == 1:
        return [0]
    local_min_idxs = []
    for i in range(len(array)):
        if i == 0 and array[i] < array[i + 1]:
            local_min_idxs.append(i)
        if i == len(array) - 1 and array[i] < array[i - 1]:
            local_min_idxs.append(i)
        if i == 0 or i == len(array) - 1:
            continue
        if array[i] < array[i + 1] and array[i] < array[i - 1]:
            local_min_idxs.append(i)
    return local_min_idxs

# def min_rewards(scores):
#     rewards = [1 for _ in scores]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(min_rewards([8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)


if __name__ == '__main__':
    unittest.main()
