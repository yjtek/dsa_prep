def change(money: int) -> int:
    count_coints = 0
    
    n_10 = money // 10
    money -= n_10 * 10
    
    n_5 = money // 5
    money -= n_5 * 5

    return n_10 + n_5 + money

if __name__ == '__main__':
    m = int(input())
    print(change(m))
