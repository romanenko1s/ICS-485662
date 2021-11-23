words = open("/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/ЛР5/Ч2/textForWordSearcher.txt").read().lower().split()

uniques = []
for word in words:
  if word not in uniques:
    uniques.append(word)

counts = []
for unique in uniques:
  count = 0
  for word in words:
    if word == unique:
      count += 1
  counts.append((count, unique))

counts.sort()
counts.reverse()
#print(counts)

for i in range(min(10, len(counts))):
  count, word = counts[i]
  print('%s %d' % (word, count))