f = open('2.txt', 'r')

INCREASE = 1
DECREASE = -1
UNINIT = 0

god_reports = 0

"""
Megvizsgáljuk az adott tömböt, hogy van e benne hiba
"""
def check_constraints(arr):
    dir = UNINIT
    for i in range(1, len(arr)):
        previous = arr[i-1]
        actual = arr[i]
        # legalább egy értéket változnia kell
        if previous == actual:
            return False
        if dir == UNINIT:
            dir = INCREASE if previous < actual else DECREASE
        else:
            # irány váltás
            if (previous < actual and dir == DECREASE) or (previous > actual and dir == INCREASE):
                return False
        # legfeljebb 3 értéket változhat
        if abs(previous-actual) > 3:
            return False
    return True

# soronként felolvassuk a fájlt és minden sort két részre bontunk a szóközök mentén
# az első részt az a listába, a második részt a b listába tesszük
while True:
    line = f.readline()
    if not line:
        break
    # egy adott sorból int listát készítünk
    arr = list(map(int, line.split()))
    if check_constraints(arr):
        god_reports += 1
    else:
        # elsőre nem ment át a riport most kipróbáljuk 1-1 elem elvétellel
        """
         2. része a feladatnak
        """
        for i in range(len(arr)):
            a = arr[:i] + arr[i+1:]
            if check_constraints(a):
                god_reports += 1
                break
f.close()

print(f"Jó riportok száma: { god_reports }")


