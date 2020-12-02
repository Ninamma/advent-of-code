import unittest

def parse_file(file_name):
    with open(file_name) as file:
        data = file.read()
    
    array_string = data.split('\n')

    return list(map(int, array_string))

def get_product(nums):
    for n in nums:
        for x in nums:
            if n == x:
                continue
            elif (n + x) == 2020:
                return n * x

class Tests(unittest.TestCase):
    def test_can_parse_file(self):
        self.assertEqual(parse_file('day1_test_input.txt'), [1721, 979, 366, 299, 675, 1456])

    def test_get_product(self):
        list_of_expenses = parse_file('day1_test_input.txt')
        self.assertEqual(get_product(list_of_expenses), 514579)
    
    def test_get_real_answer(self):
        list_of_expenses = parse_file('day1_input.txt')
        self.assertEqual(get_product(list_of_expenses), None)

if __name__ == '__main__':
    unittest.main()