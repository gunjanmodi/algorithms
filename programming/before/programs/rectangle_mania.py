import unittest

def rectangle_mania(coords):
	coords_table = get_coords_table(coords)
	print(coords_table)
	return get_rectangle_count(coords, coords_table)

def get_coords_table(coords):
	coords_table = {}
	for coord1 in coords:
		coord1_directions = {UP: [], RIGHT: [], DOWN: [], LEFT: []}
		for coord2 in coords:
			coord2_direction = get_coord_direction(coord1, coord2)
			if coord2_direction in coord1_directions:
				coord1_directions[coord2_direction].append(coord2)
		coord1_string = coord_to_string(coord1)
		coords_table[coord1_string] = coord1_directions
	return coords_table

def get_coord_direction(coord1, coord2):
	direction = ''
	x1, y1 = coord1
	x2, y2 = coord2
	if x1 == x2:
		if y1 < y2:
			direction = UP
		elif y1 > y2:
			direction = DOWN
	elif y1 == y2:
		if x1 < x2:
			direction = RIGHT
		elif x1 > x2:
			direction = LEFT
	return direction
				
def	coord_to_string(coord):
	x, y = coord
	return f"{x}-{y}"

def get_rectangle_count(coords, coords_table):
	return

UP = 'up'
RIGHT = 'right'
DOWN = 'down'
LEFT = 'left'

class TestCase(unittest.TestCase):
    def test_case_1(self):
        cords = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]
        self.assertEqual(rectangle_mania(cords), 6)


if __name__ == '__main__':
    unittest.main()