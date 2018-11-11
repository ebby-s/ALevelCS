def bracket_check(phrase):
    open_count = 0
    close_count = 0
    for i in list(phrase):
        if i == "(":
            open_count += 1
        elif i == ")":
            close_count += 1
    if open_count == close_count:
        return True
    else:
        return False
