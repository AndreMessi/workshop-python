import sys

lists = ['a', 0, 4]
for each in lists:
    try:
        print("Masukan:", each)
        r = 1/int(each)
        break
    except:
        print("Upps!", sys.exc_info()[0], " terjadi.")
        print("Masukan berikutnya.")
        print()
print("Kebalikan dari ", each, " =", r)