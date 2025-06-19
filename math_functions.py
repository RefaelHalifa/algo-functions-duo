"""ספרייה של ונקציות אלגוריתמיות נוצר ע״י רפאל כליפה ויהודה גבריאלי"""

def welcome():
    """פונקציה ברכה"""
    print("ברוכים הבאים לספרייה של פונקציות אלגוריתמיות")

if __name__ == "__main__":
    welcome()
    print(atzeret(5))
def atzeret(num: int):
    if num == 1:
        return 1
    return atzeret(num - 1) * num

print(atzeret(5))

