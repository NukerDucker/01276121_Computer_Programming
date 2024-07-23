word = input(" *** Data type integer float string ***\nEnter a word : ")
try:
    val = int(word)
    print(f"{val} * 2 = {val * 2}")
except ValueError:
    try:
        val = float(word)
        print(f"{val:.3f} / 3 = {val/3:.3f}")
    except ValueError:
        val = str(word + " ")
        print(val * 3)