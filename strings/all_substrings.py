def all_substrings(string):
    sub_set = set()
    substring_helper(string, "", sub_set)
    return sub_set


def substring_helper(in_string, out_string, sub_set):
    if len(in_string) == 0:
        if out_string:
            sub_set.add(out_string)
        return

    substring_helper(in_string[1:], out_string+in_string[0], sub_set)
    substring_helper(in_string[1:], out_string, sub_set)






# print(all_substrings("abc"))
print(all_substrings("abcd"))

# ac, abd, bd, acd, ad
