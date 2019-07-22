### huffman.py

#### [sorted排序](https://www.cnblogs.com/huchong/p/8296025.html)
```py
def parse_file(file_path):
    """
    Read the file and build a dict of all letters and their
    frequences, then convert the dict into a list of Letters.
    """
    chars = {}
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            chars[c] = chars[c] + 1 if c in chars.keys() else 1
    return sorted([Letter(c, f) for c, f in chars.items()], key=lambda l: l.freq)#按照freq排序，从小到大排序

```


#### 以下两点不懂
```py
def huffman(file_path):
    c = f.read(1)
    le = list(filter(lambda l: l.letter == c, letters))[0]
```

