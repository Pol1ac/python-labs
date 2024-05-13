def boyer_moore(haystack, needle):
    if not needle:
        return []

    shift_table = {}
    for i in range(len(needle) - 1):
        shift_table[needle[i]] = len(needle) - i - 1

    indices = []
    needle_index = len(needle) - 1

    while needle_index < len(haystack):
        haystack_index = len(needle) - 1
        current_index = needle_index

        while haystack_index >= 0 and haystack[current_index] == needle[haystack_index]:
            current_index -= 1
            haystack_index -= 1

        if haystack_index == -1:
            indices.append(needle_index - len(needle) + 1)

        if haystack[needle_index] in shift_table:
            needle_index += shift_table[haystack[needle_index]]
        else:
            needle_index += len(needle)

    return indices


haystack = "queue"
needle = "ue"
print(boyer_moore(haystack, needle)) 
