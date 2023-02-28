"""
file: decodings.py
language: python3
author: Anikhet Mulky , am9559@g.rit.edu
"""


def dp(bitstream):
    result = [0] * (len(bitstream) + 1)
    result[0] = 1

    for index in range(1, len(bitstream) + 1):
        for inside_index in range(1, 4):
            prev_bits = bitstream[index - inside_index:index]
            if len(prev_bits) == 1:
                result[index] += result[index - inside_index]
            elif prev_bits == '01' or prev_bits == '10':
                result[index] += result[index - inside_index]
            elif prev_bits == '011' or prev_bits == '111':
                result[index] += result[index - inside_index]

    return result[len(bitstream)]


def main():
    bitstream = input()
    print(dp(bitstream))


if __name__ == '__main__':
    main()
