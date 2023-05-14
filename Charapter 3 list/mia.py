nfl = ['raiders', 'patriots', '49ers', 'vikings', 'broncos', 'steelers', 'commanders']

#nfl[0] = 'pathers'
nfl.append('dolphins')
nfl.insert(3, 'ravens')
del nfl[3]

last = nfl.pop()
bad = ('broncos')
nfl.remove(bad)

print(f"\n The {bad.title()} is the badest")

print (nfl) 
print(last)