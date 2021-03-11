LETTERS = [
    *[chr(x) for x in range(ord('a'), ord('z') + 1)],
    *[chr(x) for x in range(ord('A'), ord('Z') + 1)]]


def base52_number(num: int, num_digits: int):
    arr = []
    rem = num
    for dd in range(1, num_digits + 1):
        arr.insert(0, LETTERS[rem % 52])
        rem = rem // (dd * 52)
    return ''.join(arr)


def generate_unique_keys(num_digits: int):
    for cc in range(pow(len(LETTERS), num_digits)):
        # Ensures that keys are unique
        yield base52_number(cc, num_digits)
