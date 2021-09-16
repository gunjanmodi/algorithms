
def underscorifySubstring(string, substring):
    locations = collapse(get_locations(string, substring))
    return underscorify(string, locations)


def get_locations(string, substring):
    start_index = 0
    locations = []
    while start_index < len(string):
        next_index = string.find(substring, start_index)
        if next_index != -1:
            locations.append([next_index, next_index+len(substring)])
            start_index = next_index + 1
        else:
            break
    return locations


def collapse(locations):
    if not len(locations):
        return locations
    new_locations = [locations[0]]
    previous = new_locations[0]
    for i in range(1, len(locations)):
        current = locations[i]
        if current[0] <= previous[1]:
            previous[1] = current[1]
        else:
            new_locations.append(current)
            previous = current
    return new_locations

def underscorify(string, locations):
    locations_index = 0
    string_index = 0
    in_between_underscores = False
    final_chars = []
    i = 0
    while string_index < len(string) and locations_index < len(locations):
        if string_index == locations[locations_index][i]:
            final_chars.append('_')
            i = 0 if i == 1 else 1
            in_between_underscores = not in_between_underscores
            if not in_between_underscores:
                locations_index += 1
        final_chars.append(string[string_index])
        string_index += 1
    if locations_index < len(locations):
        final_chars.append("_")
    elif string_index < len(string):
        final_chars.append(string[string_index:])
    return ''.join(final_chars)




if __name__:
    string = "testthis is a testtest to see if testestest it works"
    substring = "test"
    o = underscorifySubstring(string, substring)
    print(o)
