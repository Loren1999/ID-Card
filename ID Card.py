# coding=utf-8


import time


def id_card():

    s = "被打了****的身份证号码"

    # 根据指定的格式把一个时间字符串解析为时间元组
    first_strp_time = time.strptime(s[6:10] + '0101', '%Y%m%d')
    last_strp_time = time.strptime(s[6:10] + '1231', '%Y%m%d')
    # 返回用秒数来表示时间的浮点数,取整后得到Unix时间戳
    first_mk_time = int(time.mktime(first_strp_time))
    last_mk_time = int(time.mktime(last_strp_time)) + 1
    sfz = [
        s.replace('****', j[4:])
        for j in [time.strftime('%Y%m%d', time.localtime(i)) for i in range(first_mk_time, last_mk_time, 3600 * 24)]
        if s[-1] == '10X98765432'
        [sum(map(lambda x: int(x[0]) * x[1], zip(s.replace('****', j[4:]), [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]))) % 11]
    ]

    for i in sfz:
        print(i)


if __name__ == '__main__':
    id_card()
