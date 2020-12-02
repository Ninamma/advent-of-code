import unittest

def parse_file(file_name):
    with open(file_name) as file:
        data = file.read()
    
    array_string = data.split('\n')

    return list(map(int, array_string))

def get_product_of_two(nums):
    for n in nums:
        for x in nums:
            if n == x:
                continue
            elif (n + x) == 2020:
                return n * x

def get_product_of_three(nums):
    for n in nums:
        for x in nums:
            for y in nums:
                if (n == x) | (x == y) | (n == y):
                    continue
                elif (n + x + y) == 2020:
                    return n * x * y


class Tests(unittest.TestCase):
    def test_can_parse_file(self):
        self.assertEqual(parse_file('./inputs/day1_test_input.txt'), [1721, 979, 366, 299, 675, 1456])

    def test_get_product_of_two(self):
        list_of_expenses = parse_file('./inputs/day1_test_input.txt')
        self.assertEqual(get_product_of_two(list_of_expenses), 514579)
    
    @unittest.skip
    def test_get_part_one_answer(self):
        list_of_expenses = parse_file('./inputs/day1_input.txt')
        self.assertEqual(get_product_of_two(list_of_expenses), None)

    def test_get_product_of_three(self):
        list_of_expenses = parse_file('./inputs/day1_test_input.txt')
        self.assertEqual(get_product_of_three(list_of_expenses), 241861950)
    
        @unittest.skip
    def test_get_part_two_answer(self):
        list_of_expenses = parse_file('./inputs/day1_input.txt')
        self.assertEqual(get_product_of_three(list_of_expenses), None)


if __name__ == '__main__':
    unittest.main()