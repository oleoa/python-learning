def capital_indexes(text):
    capitals = []
    for l in range(len(text)):
        if text[l].isupper():
            capitals.append(l)
    return capitals

print(capital_indexes("HeLlO"))
