lst = list()
w = dict()
n = input("Enter ther file name and extension:")
if len(n) < 1:
    n = "mbox-short.txt"
file = open(n)

for line in file:
    if line.startswith("From "):
        array = line.split()
        time = array[5]
        hour = time.split(":")
        lst.append(hour[0])

count = 0
for word in lst:
    if word in w:
        w[word] = w.get(word, 0) + 1


    else:
        w[word] = 1

hours_and_counts = w.items()

tups = sorted(hours_and_counts)

for k, v in tups:
    print(k, v)


