"""
file: oneMatch.py
language: python3
author: Anikhet Mulky , am9559@g.rit.edu
"""


def preference(inverse_two, asker, responder):
    """
    Checking if the responder prefers the current asker to his current pair.
    """
    if inverse_two[asker] < inverse_two[responder]:
        return True
    else:
        return False


def stable_matching(num_of_elements, group_one, group_two, inverse_one, inverse_two):
    """
    We use Gale-Shapley's algorithm to find stable matching.
    """
    ask_stack = [index for index in range(num_of_elements)]
    ask_pair = ['nopair' for index in range(num_of_elements)]
    respond_pair = ['nopair' for index in range(num_of_elements)]
    count = [0] * num_of_elements

    while len(ask_stack) > 0:
        current = ask_stack.pop()   # Free asker
        while count[current] != num_of_elements:  # Until asker has asked everyone
            pref = group_one[current][count[current]]
            if respond_pair[pref] == 'nopair':   # Checking if responder has any pair
                ask_pair[current] = pref
                respond_pair[pref] = current
                count[current] += 1
                break

            elif preference(inverse_two[pref], current, respond_pair[pref]): # If responder prefers current asker
                ask_stack.append(respond_pair[pref])
                ask_pair[respond_pair[pref]] = False
                ask_pair[current] = pref
                respond_pair[pref] = current
                count[current] += 1
                break
            else:
                count[current] += 1
                continue
    return ask_pair, respond_pair


def taking_input(num_of_elements):
    """
    Storing input.
    """
    grp_one = [[] for i in range(num_of_elements)]
    grp_two = [[] for i in range(num_of_elements)]
    for index in range(num_of_elements):
        grp_one[index] = list(map(int, input().split()))
    for index in range(num_of_elements):
        grp_two[index] = list(map(int, input().split()))
    return grp_one, grp_two


def inverse(num_of_elements,grp_one,grp_two):
    """
    Inverse the array for easy preference comparison.
    """
    inverse_one = [[0] for i in range(num_of_elements)]
    inverse_two = [[0] for i in range(num_of_elements)]

    for index in range(num_of_elements):  # Preprocessing
        for inside_index in range(num_of_elements - 1):
            inverse_one[index].append(0)
            inverse_two[index].append(0)

        for inside_index in range(num_of_elements):
            inverse_one[index][grp_one[index][inside_index]] = inside_index
            inverse_two[index][grp_two[index][inside_index]] = inside_index

    return inverse_one,inverse_two


def main():
    """
    Main function.
    """
    num_of_elements = int(input())
    grp_one, grp_two = taking_input(num_of_elements) # Storing preferences
    inverse_one, inverse_two = inverse(num_of_elements, grp_one, grp_two) # Inverse the array

    # Getting the stable matching for group 1 and 2
    pair_one_ask, pair_one_resp = stable_matching(num_of_elements, grp_one, grp_two, inverse_one, inverse_two)
    pair_two_ask, pair_two_resp = stable_matching(num_of_elements, grp_two, grp_one, inverse_two, inverse_one)

    count = 0

    for x in range(num_of_elements): # Counting valid pairs
        if pair_one_ask[x] == pair_two_resp[x]:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
