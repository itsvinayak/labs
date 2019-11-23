# def greedy_knapsack(profit,weight,total_item,knapsack_capacity):
#     p_by_w_ratio=[]
#     total_profit=0
#
#     for i in range(total_item):
#         p_by_w_ratio.append(profit[i]/weight[i])
#
#     map = {}
#
#     for i,j in zip(p_by_w_ratio,range(total_item)):
#         map[i] = (profit[j],weight[j])
#
#     p_by_w_ratio.sort()
#     p_by_w_ratio.reverse()
#     print(map)
#
#     for i in p_by_w_ratio:
#         print(map[i][0],' ',map[i][1])
#         if knapsack_capacity > 0 and map[i][1] <= knapsack_capacity:
#             knapsack_capacity-=map[i][1]
#             total_profit+=map[i][0]
#             print('--> ', total_profit)
#         else:
#             break
#     if knapsack_capacity > 0:
#         total_profit=total_profit+map[p_by_w_ratio[0]][0]*(knapsack_capacity/map[p_by_w_ratio[1]][1])
#
#     return(total_profit)
#
#
# if __name__ == '__main__':
#     print(greedy_knapsack([10,5,15,7,6,18,3],[2,3,5,7,1,4,1],7,15))
#
#########################################################################


class Items:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val / wt

    def __lt__(self, other):
        return self.cost < other.cost


def getMaxValue(wt, val, capacity):
    p_by_w_ratio = []

    for i in range(len(wt)):
        p_by_w_ratio.append(Items(wt[i], val[i], i))

    p_by_w_ratio.sort(reverse=True)

    total_profit = 0

    for i in p_by_w_ratio:
        curwt = int(i.wt)
        curval = int(i.val)
        if capacity - curval >= 0:
            capacity -= curwt
            total_profit += curval
        else:
            break
    if capacity > 0:
        fraction = capacity / curwt
        total_profit += curval * fraction
        capacity = int(capacity - (curwt * fraction))

    return total_profit


if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 60

    print(getMaxValue(wt, val, capacity))
