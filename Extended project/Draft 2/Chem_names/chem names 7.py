chains = ["0","meth","eth","prop","but","pent","hex","hept","oct"]
suffixes = ["oic acid","enitrile","oate","one","ol","al","ene","yne"]
prefixes = ['methyl','ethyl','propyl','fluoro','chloro','bromo','iodo','hydroxy']
numprefixes = ["0","mono","di","tri","tetra"]

inword1 = 'methyl ethanoate'
inword2 = "2-bromo, 2,3-dichloro pent-4-ene"
inword3 = 'pent-2,4-diol'

def interpret(text):
    text = text.split()
    other_info = []
    main_info = read_main(text[-1])
    text.remove(text[-1])
    for word in text:
        other_info.append(read_group(word,prefixes))
    return [other_info,main_info]

def read_main(text):
    info = {}
    
    for prefix in prefixes:
        if prefix in text:
            info['prefix'] = prefix
            text = text.replace(prefix,'')
            break
    
    for i,chain in enumerate(chains):
        if chain in text:
            info['length'] = i
            text = text.replace(chain,'')
            break
    
    info['group'] = read_group(text,suffixes)
    return info

def read_group(text,target_list):
    info = {}
    
    for i,num in enumerate(numprefixes):
        if num in text:
            info['count'] = i
            break
    if 'count' not in info:
        info['count'] = 1
    
    info['address'] = []
    for char in text:
        try:
            char = int(char)
            info['address'].append(char)
        except:
            continue
    if len(info['address']) == 0:
        info['address'] = None
    
    for target in target_list:
        if target in text:
            info['group'] = target
            break
    return info

print(interpret(inword1))
print(interpret(inword2))
print(interpret(inword3))
