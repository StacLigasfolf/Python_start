src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

optimize = {
    i: 0 for i in src
}

for i in src:
    optimize[i] += 1

print([i for i in optimize if optimize[i] == 1])
