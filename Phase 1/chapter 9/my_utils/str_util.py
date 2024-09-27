def str_reverse(s):
    return print(s[::-1])

def substr(s, x, y):
    new_str = s[x:y]
    print(new_str)
    return new_str

if __name__ == "__main__":
    str_reverse("Yui")
    substr("Huiyuan ai", 1, 7)