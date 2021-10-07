import unittest

def parse_file(file_name):
    with open(file_name) as file:
        data = file.read()
    
    return data.split('\n')

def get_old_policies_and_passwords(lines):
    policies_and_passwords = []
    for line in lines:
        parts = line.split(' ')
        min = int(parts[0].split('-')[0])
        max = int(parts[0].split('-')[1])
        letter = parts[1][0]
        password = parts[2]
        hash = { 'min': min, 'max': max, 'letter': letter, 'password': password }
        policies_and_passwords.append(hash)
    return policies_and_passwords

def get_new_policies_and_passwords(lines):
    policies_and_passwords = []
    for line in lines:
        parts = line.split(' ')
        first_pos = int(parts[0].split('-')[0])
        second_pos = int(parts[0].split('-')[1])
        letter = parts[1][0]
        password = parts[2]
        hash = { 'positions': [first_pos, second_pos], 'letter': letter, 'password': password }
        policies_and_passwords.append(hash)
    return policies_and_passwords

def get_num_of_valid(policies_and_passwords):
    num = 0
    for policy_and_password in policies_and_passwords:
        password = policy_and_password['password']
        letter = policy_and_password['letter']
        min = policy_and_password['min']
        max = policy_and_password['max']
        count = password.count(letter)

        if count in range(min, max + 1):
            num += 1
    return num

def get_new_num_of_valid(policies_and_passwords):
    num = 0
    for policy_and_password in policies_and_passwords:
        password = policy_and_password['password']
        letter = policy_and_password['letter']
        first_pos = policy_and_password['positions'][0]
        second_pos = policy_and_password['positions'][1]

        occurrences = 0
        
        if password[first_pos - 1] == letter:
            occurrences += 1
        
        if password[second_pos - 1] == letter:
            occurrences += 1
         

        if occurrences == 1:
            num += 1
    return num

class Tests(unittest.TestCase):
    def test_parse_file(self):
        self.assertEqual(parse_file('./inputs/day2_test_input.txt')[0], '1-3 a: abcde')

    def test_old_get_policies_and_passwords(self):
        lines = parse_file('./inputs/day2_test_input.txt')
        expected = { 'min': 1, 'max': 3, 'letter': 'a', 'password': 'abcde' }
        self.assertEqual(get_old_policies_and_passwords(lines)[0], expected)
    
    def test_get_num_of_valid(self):
        lines = parse_file('./inputs/day2_test_input.txt')
        policies_and_passwords = get_old_policies_and_passwords(lines)
        num_of_valid = get_num_of_valid(policies_and_passwords)
        self.assertEqual(num_of_valid, 2)
    
    def test_get_part_one(self):
        lines = parse_file('./inputs/day2_input.txt')
        policies_and_passwords = get_old_policies_and_passwords(lines)
        num_of_valid = get_num_of_valid(policies_and_passwords)
        self.assertEqual(num_of_valid, 477)

    def test_new_get_policies_and_passwords(self):
        lines = parse_file('./inputs/day2_test_input.txt')
        expected = { 'positions': [1,3], 'letter': 'a', 'password': 'abcde' }
        self.assertEqual(get_new_policies_and_passwords(lines)[0], expected)

    def test_get_new_num_of_valid(self):
        lines = parse_file('./inputs/day2_test_input.txt')
        policies_and_passwords = get_new_policies_and_passwords(lines)
        num_of_valid = get_new_num_of_valid(policies_and_passwords)
        self.assertEqual(num_of_valid, 1)

    def test_get_part_two(self):
        lines = parse_file('./inputs/day2_input.txt')
        policies_and_passwords = get_new_policies_and_passwords(lines)
        num_of_valid = get_new_num_of_valid(policies_and_passwords)
        self.assertEqual(num_of_valid, 686)
    
if __name__ == '__main__':
    unittest.main()