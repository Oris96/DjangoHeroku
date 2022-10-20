orel_reshka, counter, counters = input() + 'О', 0, []

for i in orel_reshka:
    if i == 'О':
        counters.append(counter)
        counter = 0
    else:
        counter += 1

print(max(counters))
