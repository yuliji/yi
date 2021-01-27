import random

liushisigua = {
    0b000000: ('䷁', '坤'),
    0b000001: ('䷖', '剥'),
    0b000010: ('䷇', '比'),
    0b000011: ('䷓', '观'),
    0b000100: ('䷏', '豫'),
    0b000101: ('䷢', '晋'),
    0b000110: ('䷬', '萃'),
    0b000111: ('䷋', '否'),
    0b001000: ('䷎', '谦'),
    0b001001: ('䷳', '艮'),
    0b001010: ('䷦', '蹇'),
    0b001011: ('䷴', '渐'),
    0b001100: ('䷽', '小过'),
    0b001101: ('䷷', '旅'),
    0b001110: ('䷞', '咸'),
    0b001111: ('䷠', '遁'),
    0b010000: ('䷆', '师'),
    0b010001: ('䷃', '蒙'),
    0b010010: ('䷜', '坎'),
    0b010011: ('䷺', '涣'),
    0b010100: ('䷧', '解'),
    0b010101: ('䷿', '未济'),
    0b010110: ('䷮', '困'),
    0b010111: ('䷅', '讼'),
    0b011000: ('䷭', '升'),
    0b011001: ('䷑', '蛊'),
    0b011010: ('䷯', '井'),
    0b011011: ('䷸', '巽'),
    0b011100: ('䷟', '恒'),
    0b011101: ('䷱', '鼎'),
    0b011110: ('䷛', '大过'),
    0b011111: ('䷫', '姤'),
}


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
    gua = ['', '', '', '', '', '']
    bengua = ['', '', '', '', '', '']
    biangua = ['', '', '', '', '', '']
    for i in range(6):
        y = qigua()
        gua[i] = y
        if y == '⚋' or y == '⚊':
            bengua[i] = y
            biangua[i] = y
        elif y == 'o':
            bengua[i] = '⚊'
            biangua[i] = '⚋'
        elif y == 'x':
            bengua[i] = '⚋'
            biangua[i] = '⚊'

    y2i = {'⚋': '0', '⚊': '1'}

    print(gua)
    print(bengua)
    bengua_idx = int(''.join([y2i[y] for y in bengua]), 2)
    if bengua_idx in liushisigua:
        print(liushisigua[bengua_idx])
    print(biangua)
    biangua_idx = int(''.join([y2i[y] for y in biangua]), 2)
    if biangua_idx in liushisigua:
        print(liushisigua[biangua_idx])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
