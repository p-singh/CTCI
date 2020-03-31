
def is_unique(s: str):
    char_set= set()
    for c in s:
        if c in char_set:
            return False
        else:
            char_set.add(c)
    return True


if __name__ == "__main__":
    print(is_unique("ab22s"))