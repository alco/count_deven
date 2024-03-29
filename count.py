NDIGITS = 5  # == len([1, 3, 5, 7, 9])


def num_to_digits(num):
    """
    Convert the given number to a list of decimal digits:

      123 -> [3, 2, 1]

    """
    result = []
    while num > 0:
        digit = num % 10
        result.append(digit)
        num /= 10
    return result

def total_odd(ndigits):
    """Count all dodd numbers that have `ndigits` digits"""
    return NDIGITS ** ndigits

def count_valid_digits(digit):
    """Count how many odd digits there are when counting from `digit`"""
    return (9 - digit) / 2 + 1

def count_above(digits):
    """Count all dodd numbers that have `len(digits)` digits starting from `digits`"""
    count = 0
    accum = 1
    for digit in digits:
        cnt = count_valid_digits(digit)
        if accum > 1:
            count += (cnt-1) * accum #pow(NDIGITS, to_the_right)
        else:
            count += cnt
        accum *= NDIGITS
    return count

def count_odd(left, right):
    """Count all dodd numbers between `left` and `right`, inclusive"""
    left_digits = num_to_digits(left)
    left_count = count_above(left_digits)

    right_digits = num_to_digits(right)
    right_count = count_above(right_digits)

    n = len(right_digits) - len(left_digits)
    if n == 0:
        return left_count - right_count + 1
    else:
        count = left_count + total_odd(len(right_digits)) - right_count + 1

    if n > 1:
        for i in range(len(left_digits)+1, len(right_digits)):
            count += total_odd(i)

    return count

if __name__ == '__main__':
    # There is a piece of missing functionality here.
    #
    # Function dodd_left(left) would take a left bound and produce the smallest
    # dodd number >= left.
    #
    # Function dodd_right(right) would take a right bound and produce the
    # largest dodd number <= right.
    #
    # If dodd_left(left) > left, for example, it is guaranteed that all numbers
    # between those two will be deven.
    #
    # Implementation of those two functions is left as an exercise. The bounds
    # `left` and `right` below are intentially dodd as if there have already
    # been transoformed by the said functions.
    left = 1
    right = int("1" * 10000)

    total_count = right - left
    dodd_count = count_odd(left, right)
    even_count = total_count - dodd_count + 1
    print "even count =", even_count

    # $ time python count.py
    # ...
    # python count.py  0.69s user 0.01s system 99% cpu 0.703 total
