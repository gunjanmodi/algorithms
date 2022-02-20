"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

# Time: O()
# Space: O()


def main(string):
    if not string:
        return -1

    if len(string) % 2 != 0:
        return -1

    stack = [string[0]]
    for i in range(1, len(string)):
        token = string[i]
        if token == "}" and stack[-1] == "{":
            stack.pop()
        else:
            stack.append(string[i])

    toggle = '{'
    count = 0
    for i in range(len(stack)):
        token = stack[i]
        if token != toggle:
            count += 1
        toggle = "}" if toggle == "{" else "{"
    return count






# Test case 1: Normal or Given input
print(main("}{{}}{{{"))
# Test case 2: Normal or Given input
print(main("{{}{{{}{{}}{{"))
# Test case 3: Normal or Given input
# print(main())
# Test case 4: Negative
print(main("}{"))
# Test case 5: Empty
print(main(""))
# Test case 6: Too long
print(main("{{{{{}}}}}{{"))
# Test case 7
# Test case 8
# Test case 9