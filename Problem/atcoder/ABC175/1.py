s = input()
print(type(s))
if s == "SSS":
    print(0)
elif s == "RSS" or s == "SRS" or s == "SSR" or s == "RSR":
    print(1)
elif s == "RRS" or s == "SRR":
    print(2)
elif s == "RRR":
    print(3)
else:
    print(4)

# if s.count("R") == 0:
#     print(0)
# elif s.count("R") == 1 or s == "RSR":
#     print(1)
# elif s.count("R") == 2:
#     print(2)
# elif s.count("R") == 3:
#     print(3)
