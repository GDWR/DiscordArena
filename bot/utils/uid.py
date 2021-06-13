import random


def convert_b34(n: int, length: int = 4, _c: str = "123456789ABCDEFGHJKLMNOPQRSTUVWXYZ") -> str:
    """
    Convert an integer to Base34 (uppercase ASCII and digits, excluding 0 and I)

    :param n: The value to retrieve in Base34
    :param length: The length of the UID to retrieved
    :param _c: The characters used
    :return: Converted value
    """
    chars = [_c[0]] * length
    while n:
        length -= 1
        chars[length] = _c[n % len(_c)]
        n //= len(_c)
    return ''.join(chars)


def get_uid(user_id: int, n: int) -> str:
    """
    Get the next UID for the user.
    Max `n` value is 46,376.

    :param user_id: The UID of the user is used to generate UIDs sequences.
    :param n: The index in the sequence to gather
    :return: UID specific to that user
    """
    random.seed(user_id)
    for _ in range(n):  # Cycle the Random state.
        n = random.randint(0, 1_336_336)  # 1336336 is max permutations
    return convert_b34(n)
