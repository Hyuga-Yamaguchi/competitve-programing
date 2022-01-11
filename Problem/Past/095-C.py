A, B, C, X, Y = map(int, input().split())

cost_list = []
for i in range(0, max([X, Y]) * 2 + 1, 2):
    AB_cost = C * i
    A_cost = A * (X - int(i / 2))
    B_cost = B * (Y - int(i / 2))
    if A_cost < 0 and B_cost >= 0:
        A_cost = 0
    elif A_cost >= 0 and B_cost < 0:
        B_cost = 0
    elif A_cost >= 0 and B_cost >= 0:
        pass
    else:
        A_cost = 0
        b_cost = 0
    cost = AB_cost + A_cost + B_cost
    cost_list.append(cost)
print(cost_list)
print(min(cost_list))
