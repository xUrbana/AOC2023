from typing import List


def get_first_last_digit_numeric(s: str) -> tuple:
    first_digit = None
    last_digit = None
    for c in s:
        if c.isdigit():
            last_digit = c
            if first_digit is None:
                first_digit = c
    return first_digit, last_digit


def build_trie(words: List[tuple]) -> dict:
    root = {}
    for word, val in words:
        cur = root
        for letter in word:
            cur = cur.setdefault(letter, {})
        cur["_end_"] = val
    return root


def get_first_last_digit_words(s: str) -> tuple:
    root_trie = build_trie(
        (
            ("one", "1"),
            ("two", "2"),
            ("three", "3"),
            ("four", "4"),
            ("five", "5"),
            ("six", "6"),
            ("seven", "7"),
            ("eight", "8"),
            ("nine", "9"),
        )
    )

    trie = root_trie
    first_digit = None
    last_digit = None

    for c in s:
        # If its a digit, store it and move on
        if c.isdigit():
            last_digit = c
            if first_digit is None:
                first_digit = c
            continue

        if c in trie:
            trie = trie[c]
        else:
            trie = root_trie
            if c in trie:
                trie = trie[c]

        if (num := trie.get("_end_")) is not None:
            last_digit = num
            if first_digit is None:
                first_digit = num

    return first_digit, last_digit


def get_calibration_values_numeric(fp) -> None:
    for line in fp:
        first_digit, last_digit = get_first_last_digit_numeric(line)
        yield int(first_digit + last_digit)


def get_calibration_values_words(fp) -> None:
    for line in fp:
        first_digit, last_digit = get_first_last_digit_words(line)
        yield int(first_digit + last_digit)


def solve_p1() -> None:
    with open("input.txt") as fp:
        return sum(get_calibration_values_numeric(fp))


def solve_p2() -> None:
    with open("input.txt") as fp:
        return sum(get_calibration_values_words(fp))


if __name__ == "__main__":
    print(f"d1p1 = {solve_p1()}")
    print(f"d1p2 = {solve_p2()}")
