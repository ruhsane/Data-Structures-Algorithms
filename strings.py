#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # text will never contain the pattern if pattern is larger
    if len(pattern) > len(text):        
        return False
    if pattern == "":
        return True

    current_text_index = 0
    current_pattern_index = 0

    while current_text_index != len(text):
        
        if text[current_text_index] == pattern[current_pattern_index]:
            current_pattern_index += 1
            current_text_index += 1

            if current_pattern_index == len(pattern):
                return True
        else:
            if current_pattern_index != 0:
                current_text_index = current_text_index - current_pattern_index + 1
            else:
                current_text_index += 1
            current_pattern_index = 0

    return False
    

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # text will never contain the pattern if pattern is larger
    if len(pattern) > len(text):        
        return None
    if pattern == "":
        return 0

    current_text_index = 0
    current_pattern_index = 0

    while current_text_index != len(text):
        
        if text[current_text_index] == pattern[current_pattern_index]:
            current_pattern_index += 1
            current_text_index += 1

            if current_pattern_index == len(pattern):
                return current_text_index - len(pattern) 
        else:
            if current_pattern_index != 0:
                current_text_index = current_text_index - current_pattern_index + 1
            else:
                current_text_index += 1
            current_pattern_index = 0

    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    indexes_list = []

    # text will never contain the pattern if pattern is larger
    if len(pattern) > len(text):        
        return indexes_list
    if pattern == "":
        for i in range(len(text)):
            indexes_list.append(i)
        return indexes_list

    current_text_index = 0
    current_pattern_index = 0

    while current_text_index != len(text):
        
        if text[current_text_index] == pattern[current_pattern_index]:
            current_pattern_index += 1
            current_text_index += 1

            if current_pattern_index == len(pattern):
                indexes_list.append(current_text_index - len(pattern))
                current_text_index = current_text_index - current_pattern_index + 1
                current_pattern_index = 0

        else:
            if current_pattern_index != 0:
                current_text_index = current_text_index - current_pattern_index + 1
            else:
                current_text_index += 1
            current_pattern_index = 0

    return indexes_list

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()