def vowel_count(text):
    vowels = ["a","e","i","o","u"]
    count = 0
    for i in range(len(text)):
        if text[i] in vowels:
            count += 1
    if count >= 3:
        return True
    else:
        return False

def repetition(text):
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            return True
    return False

def forbidden(text):
    forbidden = ["ab","cd","pq","xy"]
    for phrase in forbidden:
        if phrase in text:
            return False
    return True



def is_nice(text):
    if vowel_count(text) and repetition(text) and forbidden(text):
        return True
    else:
        return False
    
    
