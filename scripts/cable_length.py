# Convert coordinate pair to a nice formatted string
def coords(x, y):
    letters = "ABCDEFG"
    return "{}{}".format(letters[y], x+1)

cuts = []

for x in range(7):
    for y in range(7):
        xlength = 12 - 2 * x
        ylength = 2 * abs(y - 3)
        pad = 2.7
        total = xlength + ylength + pad
        cuts.append((total, x, y))
        print("LED {}: {}m + {}m + {}m = {}m".format(coords(x,y), xlength,
                                                     ylength, pad, total))

print("\nTotal length: {:.1f}\n".format(sum([c[0] for c in cuts])))

bins = [[], [], [], [], [], []]
unbinned = []

for cut in reversed(sorted(cuts, key=lambda cut: cut[0])):
    length = cut[0]
    for b in bins:
        if 100.0 - sum([c[0] for c in b]) >= length:
            b.append(cut)
            break
    else:
        unbinned.append(cut)

for idx, b in enumerate(bins):
    print("Bin {}: {}".format(idx, ', '.join(
        ["{:.2f}m".format(c[0]) for c in b])))
    print("Total length: {:.1f}m\n".format(sum([c[0] for c in b])))
print(unbinned)
print("Unbinned: {}".format(', '.join(["{}m ".format(c[0]) for c in unbinned])))


# Cutting list:
print("")
print("")
print("--== CUTTING LIST ==--")
for idx, b in enumerate(bins):
    print("--- Reel {} ---".format(idx+1))
    for cut in b:
        print("{}: {:.1f}m\t[ ]".format(coords(cut[1], cut[2]), cut[0]))
    print("")

print("--- Leftover ---")
for cut in unbinned:
    print("{}: {:.1f}m\t[ ]".format(coords(cut[1], cut[2]), cut[0]))
