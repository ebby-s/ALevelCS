
import random

artist1=['song1','song2','song3','song4','song5','song6','song7','song8','song9','song10']
artist2=['mel1','mel2','mel3','mel4','mel5','mel6','mel7','mel8','mel9','mel10']
artist3=['comp1','comp2','comp3','comp4','comp5','comp6','comp7','comp8','comp9','comp10']
artist4=['rap1','rap2','rap3','rap4','rap5','rap6','rap7','rap8','rap9','rap10']
artist5=['gui1','gui2','gui3','gui4','gui5','gui6','gui7','gui8','guit9','gui10']
artist6=['piano1','piano2','piano3','piano4','piano5','piano6','piano7','piano8','piano9','piano10']
artist7=['DJ1','DJ2','DJ3','DJ4','DJ5','DJ6','DJ7','DJ8','DJ9','DJ10']
artist8=['sad1','sad2','sad3','sad4','sad5','sad6','sad7','sad8','sad9','sad10']
artist9=['hap1','hap2','hap3','hap4','hap5','hap6','hap7','hap8','hap9','hap10']
artist10=['tal1','tal2','tal3','tal4','tal5','tal6','tal7','tal8','tal9','tal10']

artists = [artist1, artist2, artist3, artist4, artist5, artist6, artist7, artist8, artist9, artist10]
random.shuffle(artists)

playlists = [artists[0]+artists[3]+artists[6],artists[1]+artists[4]+artists[7],artists[2]+artists[5]+artists[8]]
final = []


for i in range(30):
    for playlist in playlists:
        final.append(playlist[i])
final += artists[9]
    
print(final)
