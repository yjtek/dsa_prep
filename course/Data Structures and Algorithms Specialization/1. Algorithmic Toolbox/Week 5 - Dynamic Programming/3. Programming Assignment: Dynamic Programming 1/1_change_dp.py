results = {}

def change(money):
    if money <= 0:
        return 0    
    if money in results:
        return results.get(money)

    count1 = change(money-1) + 1
    count3 = change(money-3) + 1
    count4 = change(money-4) + 1
    # print(count1, count3, count4)
    results[money] = min(count1, count3, count4)
    return results.get(money)

if __name__ == '__main__':
    m = int(input())
    print(change(m))
