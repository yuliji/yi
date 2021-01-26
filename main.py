import random


def qigua():
    a = random.randint(0, 1)
    b = random.randint(0, 1)
    c = random.randint(0, 1)
    total = a + b + c
    print(f"{a} {b} {c}")
    if total == 0:
        # 三个反面是老阳，主卦为阳，变卦为阴
        return "o"
    elif total == 1:
        # 一个正面为少阴
        return "⚋"
    elif total == 2:
        # 两个正面为少阳
        return "⚊"
    elif total == 3:
        # 三个正面是老阴， 主卦为阴， 变卦为阳
        return "x"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    yao = ['', '', '', '', '', '']
    for i in range(6):
        yao[i] = qigua()
    print(yao)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
