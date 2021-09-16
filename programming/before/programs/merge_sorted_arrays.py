import unittest


# def merge_sorted_arrays(arrays):
#     sorted_array = []
#     indices_ref = [0 ] * len(arrays)
#     while True:
#         selected_items = []
#         for i in range(len(arrays)):
#             current_array = arrays[i]
#             element_index = indices_ref[i]
#             if element_index == len(current_array):
#                 continue
#             selected_items.append({"index": i, "num": current_array[element_index]})
#         if len(selected_items) == 0:
#             break
#         min_item = get_min_for_selected(selected_items)
#         sorted_array.append(min_item['num'])
#         indices_ref[min_item['index']] += 1
#     return sorted_array

# def get_min_for_selected(items):
#     idx = 0
#     min_item = items[0]
#     for idx in range(1, len(items)):
#         if items[idx]['num'] < min_item['num']:
#             min_item = items[idx]
#     return min_item

# ----------- SECOND SOLUTION -----------
def merge_sorted_arrays(arrays):
    sorted_list = []
    smallest_items = []
    for array_idx in range(len(arrays)):
        smallest_items.append({"array_idx": array_idx, "element_idx": 0, "num": arrays[array_idx][0]})
    min_heap = MinHeap(smallest_items)
    while not min_heap.is_empty():
        smallest_item = min_heap.remove()
        array_idx, element_idx, num = smallest_item['array_idx'], smallest_item['element_idx'], smallest_item['num']
        sorted_list.append(num)
        if element_idx == len(arrays[array_idx]) - 1:
            continue
        min_heap.insert({'array_idx': array_idx, 'element_idx': element_idx + 1, 'num': arrays[array_idx][element_idx + 1]})
    return sorted_list


class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
        
    def is_empty(self):
        return len(self.heap) == 0

    def buildHeap(self, array):
        first_parent_index = (len(array) - 2) // 2
        for current_index in reversed(range(first_parent_index + 1)):
            self.siftDown(current_index, len(array) - 1, array)
        return array
        

    def siftDown(self, current_index, end_index, heap):
        child_one_index = current_index * 2 + 1
        while child_one_index <= end_index:
            child_two_index = 2 * current_index + 2 if current_index * 2 + 2 <= end_index else -1
            if child_two_index != -1 and heap[child_two_index]["num"] < heap[child_one_index]["num"]:
                index_to_swap = child_two_index
            else:
                index_to_swap = child_one_index
            if heap[index_to_swap]["num"] < heap[current_index]["num"]:
                self.swap(current_index, index_to_swap, heap)
                current_index = index_to_swap
                child_one_index = 2 * current_index + 1
            else:
                return

    def siftUp(self, current_index, heap):
        parent_index = (current_index - 1) // 2
        while current_index > 0 and heap[current_index]["num"] < heap[parent_index]["num"]:
            self.swap(current_index, parent_index, heap)
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return value_to_remove
        

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
        
    def swap(self, idx1, idx2, heap):
        heap[idx1], heap[idx2] = heap[idx2], heap[idx1]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrays = [
            [1, 5, 9, 21],
            [-1, 0],
            [-124, 81, 121],
            [3, 6, 12, 20, 150],
        ]
        output = merge_sorted_arrays(arrays)
        self.assertEqual(output, [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150])

if __name__ == '__main__':
    unittest.main()