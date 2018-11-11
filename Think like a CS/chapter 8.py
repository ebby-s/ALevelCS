prefixes = "JKLMNOPQ"
suffix = "uack"

for letter in prefixes:
    print(letter + suffix)

def count_letters(string,letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    print(count)

def count_letters2(string,letter):
    count = -1
    pos = 0
    check_pos = 0
    while pos != -1:
        pos = string.find(letter,check_pos)
        check_pos = pos + 1
        count += 1
    print(count)

fave_text = """Freeman and slave, patrician and plebeian, lord and serf, guild-master and journeyman,
in a word, oppressor and oppressed, stood in constant opposition to one another, carried on an uninterrupted,
now hidden, now open fight, a fight that each time ended, either in a revolutionary reconstitution of society
at large, or in the common ruin of the contending classes.
In the earlier epochs of history, we find almost everywhere a complicated arrangement of society into
various orders, a manifold gradation of social rank. In ancient Rome we have patricians, knights, plebeians,
slaves; in the Middle Ages, feudal lords, vassals, guild-masters, journeymen, apprentices, serfs; in almost
all of these classes, again, subordinate gradations.
The modern bourgeois society that has sprouted from the ruins of feudal society has not done away with
class antagonisms. It has but established new classes, new conditions of oppression, new forms of struggle
in place of the old ones.
Our epoch, the epoch of the bourgeoisie, possesses, however, this distinct feature: it has simplified
class antagonisms. Society as a whole is more and more splitting up into two great hostile camps, into
two great classes directly facing each other — Bourgeoisie and Proletariat."""

def word_count(text):
    punc_list = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    no_punc = ""
    for letter in text:
        if letter not in punc_list:
            no_punc += letter
    text = no_punc.split(" ")
    e_count = 0
    for word in text:
        if "e" in word:
            e_count += 1
    print('Your text contains {0} words, of which {1} ({2}%) contain an "e".'.format(str(len(text)),str(e_count),str(e_count/len(text)*100)))
    

layout = "{0:>3}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}"

print(layout.format("1","2","3","4","5","6","7","8","9","10","11","12"))
for i in range(2,13):
      print(layout.format(i,2*i,3*i,4*i,5*i,6*i,7*i,8*i,9*i,10*i,11*i,12*i))

def reverse(text):
    return text[::-1]

def mirror(text):
    return text + reverse(text)

def remove_letter(letter,text):
    for char in text:
        if char == letter:
            text = text.replace(char,'')
    return text

def is_palindrome(text):
    return text == reverse(text)

def count(sub,text):
    count = -1
    pos = 0
    check_pos = 0
    while pos != -1:
        pos = text.find(sub,check_pos)
        check_pos = pos + 1
        count += 1
    return(count)

def remove(sub,text):
    if sub in text:
        return text.replace(sub,"",1)

def remove_all(sub,text):
    if sub in text:
        return text.replace(sub,"")


