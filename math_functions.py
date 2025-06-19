"""ספרייה של ונקציות אלגוריתמיות נוצר ע״י רפאל כליפה ויהודה גבריאלי"""

def welcome():
    """פונקציה ברכה"""
    print("ברוכים הבאים לספרייה של פונקציות אלגוריתמיות")

def is_prime(n, i=2):
    if n <= 1:
        return False
    if i > n // 2:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

if __name__ == "__main__":
    welcome()
    print(is_prime(7))