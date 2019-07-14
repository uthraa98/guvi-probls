def LexicographicalMaxString(str):
    mx = ""
    for i in range(len(str)):
        mx = max(mx, str[i:])
    return mx
if __name__ == '__main__':
    str = input()
    print(LexicographicalMaxString(str))
