"""
当前目录下有一个文件名为btc_price.txt的文件，存储着2018年第一季度比特币的价格，共有时间、价格两列，请计算第一季度每个月比特币的平均价格，并按照价格由低到高的顺序，将数据以月份、价格两列存放到另一文件btc_price_season1.txt中，并在屏幕上以字典的形式输出。
"""

with open("btc_price.txt", encoding="utf-8") as fp:
    monthMoney = [0, 0, 0, 0]
    monthDay = [0, 0, 0, 0]
    monthPrice = {}
    for line in fp:
        s = line.split(" ")  # 分割钱和月份
        n = int(s[0][6])  # 得到月份
        monthMoney[n - 1] += float(s[1])
        monthDay[n - 1] += 1

    for i in range(4):
        monthPrice[i + 1] = monthMoney[i] / monthDay[i]
    sort = sorted(monthPrice, key=lambda x: monthPrice[x])  # 排序

file_r = open('btc_price_season1.txt', 'w', encoding='utf-8')  # 生成新的文件
for i in sort:
    file_r.write(str(i) + " " + str(monthPrice[i]) + "\n")
print(monthPrice)  # 以字典输出
file_r.close()
