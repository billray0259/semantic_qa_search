
base = "https://people.cs.umass.edu/~mcgregor/514S22/lecture"

with open("data/cs514.txt", "w") as f:
    for i in range(1, 25):
        url = base + str(i) + ".pdf"
        f.write(url + "\n")