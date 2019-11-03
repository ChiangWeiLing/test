import sys


def calculate_fee(i, electron_number):

    if i >= 6 & i <= 9:
        if electron_number <= 120:
            return electron_number * 2 * 1.63
        elif electron_number>120 & electron_number<=330:
            return 2.38*((electron_number-120)*2)+(120*2*1.63)
        elif electron_number>330 & electron_number<=500:
            return (3.52*((electron_number-330)*2))+(110*2.38*2)+(120*2*1.63)
        elif electron_number>500 & electron_number<=700:
            return (4.80*((electron_number-500)*2))+(170*3.52*2)+(110*2.38*2)+(120*2*1.63)
        elif electron_number>700 & electron_number<=1000:
            return (5.66*((electron_number-700)*2))+(200*4.80*2)+(170*3.52*2)+(110*2.38*2)+(120*2*1.63)
        else:
            return (6.41*((electron_number-1000)*2))+(300*5.66*2)+(200*4.80*2)+(170*3.52*2)+(110*2.38*2)+(120*2*1.63)
    # print("夏季用電:"+fee+"元")

    if not((i >= 6) & (i <= 9)):
        if electron_number <= 120:
            return electron_number * 2 * 1.63
        elif electron_number > 120 & electron_number <= 330:
            return 2.10 * ((electron_number-120) * 2)+(120 * 2 * 1.63)
        elif electron_number > 330 & electron_number <= 500:
            return (2.89 * ((electron_number-330) * 2))+(110 * 2.10 * 2)+(120 * 2 * 1.63)
        elif electron_number > 500 & electron_number <= 700:
            return (3.94 * ((electron_number-500) * 2))+(170 * 2.89 * 2)+(110 * 2.10 * 2)+(120 * 2 * 1.63)
        elif electron_number > 700 & electron_number <= 1000:
            return (4.60 * ((electron_number-700) * 2))+(200 * 3.94 * 2)+(170 * 2.89 * 2)+(110 * 2.10 * 2)+(120 * 2 * 1.63)
        else:
            return (5.03 * ((electron_number-1000) * 2))+(300 * 4.60 * 2)+(200 * 3.94 * 2)+(170 * 2.89 * 2)+(110 * 2.10 * 2)+(120 * 2 * 1.63)
    # print("非夏季用電:"+fee+"元")

print('請輸入月份(1~12):')
month = int(sys.stdin.readline().strip('\n'))
print('請輸入該月用電量:')
electron_number = int(sys.stdin.readline().strip('\n'))
print(f'{month}月份，電費共計 {calculate_fee(month,electron_number)} 元。')