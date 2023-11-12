
def permutations(prefix, original):

    if len(prefix) == len(original):
        print(prefix)
        return

    for letter in original:
        if letter not in prefix:
            permutations(prefix + letter, original)


permutations('', '0123456789')
