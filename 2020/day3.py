import unittest

def parse_file(file_name):
    with open(file_name) as file:
        data = file.read()
    
    return data.split('\n')

def move(units, map):
    x_max = len(map[0])
    x_pos = 3 * units
    if x_pos >= x_max:
        x_pos -= x_max 

    finish = [x_pos, units]

    return map[finish[1]][finish[0]]

class Tests(unittest.TestCase):
    def test_parse_file(self):
        self.assertEqual(parse_file('./inputs/day3_test_input.txt')[0], '..##.......')

    def test_can_move_one_slope_unit(self):
        map = parse_file('./inputs/day3_test_input.txt')
        final_spot = move(1, map)
        self.assertEqual(final_spot, '.')
    

    def test_can_move_two_slope_units(self):
        map = parse_file('./inputs/day3_test_input.txt')
        final_spot = move(2, map)
        self.assertEqual(final_spot, '#')
    
    def test_can_move_three_slope_units(self):
        map = parse_file('./inputs/day3_test_input.txt')
        final_spot = move(3, map)
        self.assertEqual(final_spot, '.')
    
    def test_can_move_four_slope_units_and_wrap_around(self):
        map = parse_file('./inputs/day3_test_input.txt')
        final_spot = move(4, map)
        self.assertEqual(final_spot, '#')
    
    def test_can_move_five_slope_units_and_wrap_around(self):
        map = parse_file('./inputs/day3_test_input.txt')
        final_spot = move(5, map)
        self.assertEqual(final_spot, '#')
    
    def test_can_move_to_end_of_map(self):
        map = parse_file('./inputs/day3_test_input.txt')
        map_size = len(map)
        print(map_size)
        final_spot = move(map_size - 1, map)
        self.assertEqual(final_spot, '#')

    # def test_can_count_how_many_trees(self):
    #     map = parse_file
    
if __name__ == '__main__':
    unittest.main()