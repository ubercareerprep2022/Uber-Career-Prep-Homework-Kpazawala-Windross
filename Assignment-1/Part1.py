
def isStringPermutation(s1: str, s2: str) -> bool:
    holder = 0
    for char in s1:
        if char not in s2:
            return False
        else:
            holder += 1
    if holder == len(s2):
        return True


if __name__ == "__main__":
    print(
        isStringPermutation("asdf", "fsda"),
        isStringPermutation("asdf", "fsa"),
        isStringPermutation("asdf", "fsax"),
    )
