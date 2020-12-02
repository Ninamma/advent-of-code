import unittest
from itertools import combinations

def parse_file(file_name):
    with open(file_name) as file:
        data = file.read()
    
    array_string = data.split('\n')

    return list(map(int, array_string))

def get_entries(nums, num_of_entries):
    combos = combinations(nums, num_of_entries)
    
    for combo in combos:
        if sum(combo) == 2020:
            return combo

def get_product(nums):
    product = 1
    for num in nums:
        product *= num

    return product
    
class Tests(unittest.TestCase):
    def test_can_parse_file(self):
        self.assertEqual(parse_file('./inputs/day1_test_input.txt'), [1721, 979, 366, 299, 675, 1456])

    def test_get_product_of_two(self):
        list_of_expenses = parse_file('./inputs/day1_test_input.txt')
        entries = get_entries(list_of_expenses, 2)
        self.assertEqual(get_product(entries), 514579)
    
    @unittest.skip
    def test_get_part_one_answer(self):
        list_of_expenses = parse_file('./inputs/day1_input.txt')
        entries = get_entries(list_of_expenses, 2)
        self.assertEqual(get_product(entries), None)

    def test_get_product_of_three(self):
        list_of_expenses = parse_file('./inputs/day1_test_input.txt')
        entries = get_entries(list_of_expenses, 3)
        self.assertEqual(get_product(entries), 241861950)
    
    @unittest.skip
    def test_get_part_two_answer(self):
        list_of_expenses = parse_file('./inputs/day1_input.txt')
        entries = get_entries(list_of_expenses, 3)
        self.assertEqual(get_product(entries), None)

if __name__ == '__main__':
    unittest.main()