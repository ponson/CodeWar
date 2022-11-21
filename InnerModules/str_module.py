def str_trans():
    s = 'abc123xyz'
    print(s.translate(str.maketrans('abcxyz', 'xyzabc')))
    

if __name__ == "__main__":
    str_trans()