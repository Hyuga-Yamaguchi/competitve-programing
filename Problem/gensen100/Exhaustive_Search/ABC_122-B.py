s = input()
ls = len(s)

ans = 0
for i in range(ls):
    for j in range(i, ls + 1):
        ns = s[i:j]
        #print(ns)
        if len(ns) == ns.count("A") + ns.count("G") + ns.count("C") + ns.count("T"):
            ans = max(ans, len(ns))
print(ans)
