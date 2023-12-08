import re

# Exo 1
fichier = open('index.html', 'r')
content = fichier.read()
print(content)

# Exo 2
# motif = r'<a\s+(?:[^>]*?\s+)?href=(["\'])((https?:\/\/|www\.).*?)\1'
# res = re.findall(motif, content)
# for r in res:
#     print(r[1])

# Exo 3
# motif = r'<a\s+(?:[^>]*?\s+)?href=(["\'])((https?:\/\/|www\.)\S*?article\S*?)\1'
# res = re.findall(motif, content)
# for r in res:
#     print(r[1])

# Exo 4 et 5
motif = r'<a\s+(?:[^>]*?\s+)?href=(["\'])((https?:\/\/|www\.)\S*?article\S*?)\1'
res = re.findall(motif, content)
all_dates = {}
for r in res:
    date = ""
    for s in r[1].split('/'):
        if re.match(r'^\d{4}$', s):
            date += s
        elif re.match(r'^\d{2}$', s):
            date += "-" + s
    if date in all_dates:
        all_dates[date] += 1
    else:
        all_dates[date] = 1
    print(date)

print(all_dates)

# Exo 6
f = open('stats.txt', 'w')

data = "{"
i = 1
for date in all_dates:
    if all_dates.__len__() == i:
        data += "'" + date + "': " + str(all_dates[date]) + "}"
    else:
        data += "'" + date + "': " + str(all_dates[date]) + ", "
        if i % 3 == 0:
            data += "\n"
    i += 1

print(data)
f.write(data)
f.close()