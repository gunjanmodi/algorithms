import unittest

def longestStringChain(strings):
    string_chains = {}
    for string in strings:
        string_chains[string] = {"next_string": "", "max_string_length": 1}

    sorted_strings = sorted(strings, key=len)

    for string in sorted_strings:
        find_longest_string_chain(string, string_chains)
    return build_longest_string_chain(strings, string_chains)

def find_longest_string_chain(string, string_chains):
    for i in range(len(string)):
        smaller_string = get_smaller_string(string, i)
        if smaller_string not in string_chains:
            continue
        try_update_string_chains(string, smaller_string, string_chains)


def get_smaller_string(string, index):
    return string[0:index] + string[index + 1:]

def try_update_string_chains(level_two_string, smaller_string, string_chains):
    smaller_string_length = string_chains[smaller_string]["max_string_length"]
    current_string_length = string_chains[current_string]["max_string_length"]

    if smaller_string_length + 1 > current_string_length:
        string_chains[current_string]["max_string_length"] = smaller_string_length + 1
        string_chains[current_string]["next_string"] = smaller_string

def build_longest_string_chain(strings, string_chains):
    max_chain_length = 0
    chain_starting_string = ""
    for string in strings:
        if string_chains[string]["max_string_length"] > max_chain_length:
            max_chain_length = string_chains[string]["max_string_length"]
            chain_starting_string = string

    our_longest_string_chain = []
    current_string = chain_starting_string
    while current_string != "":
        our_longest_string_chain.append(current_string)
        current_string = string_chains[current_string]["next_string"]
    return [] if len(our_longest_string_chain) == 1 else our_longest_string_chain

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
        expected = ["abcdef", "abcde", "abde", "ade", "ae"]
        self.assertEqual(longestStringChain(strings), expected)


if __name__ == '__main__':
    unittest.main()
