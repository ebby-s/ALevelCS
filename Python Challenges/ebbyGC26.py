def test():
    test_phrase = "this phrase"
    print(test_phrase)
    attempt = input("Type in the phrase above: ")
    if test_phrase == attempt:
        return True
    else:
        return False
