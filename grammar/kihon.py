# coding: utf-8 # 日本語使えるようにする
# コメントアウトは#

# 関数定義
def add(x1, x2):
    return x1 + x2

a = 3
b = 6
print("{} + {} = {}".format(a, b, add(a, b)))


def sum_of_list(number_list):
    total = 0
    for number in number_list: # listの要素分繰り返される
        total += number

    return total

number_list = [1,2,3,4,5]

print("リストの合計は", sum_of_list(number_list))
