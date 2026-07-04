with open("data.csv", "r", encoding="utf-8") as f:
    for i in range(3):
        print(repr(f.readline()))