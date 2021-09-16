def generate_div_tags(num_of_tags):
    matched_div_tags = []
    generate_div_tags_from_prefix(num_of_tags, num_of_tags, "", matched_div_tags)
    return matched_div_tags


def generate_div_tags_from_prefix(opening_tags_needed, closing_tags_needed, prefix, result):
    if opening_tags_needed > 0:
        new_prefix = prefix + "<div>"
        generate_div_tags_from_prefix(opening_tags_needed - 1, closing_tags_needed, new_prefix, result)

    if opening_tags_needed < closing_tags_needed:
        new_prefix = prefix + "</div>"
        generate_div_tags_from_prefix(opening_tags_needed, closing_tags_needed - 1, new_prefix, result)

    if closing_tags_needed == 0:
        result.append(prefix)


if __name__ == '__main__':
    result = generate_div_tags(3)
    print(result)