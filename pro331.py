def LexicographicalMaxString(t):
    mx = ""
    for i in range(len(t)):
        mx = max(mx, t[i:])
    return mx
if __name__ == '__main__':
    t = input()
    print(LexicographicalMaxString(t))
