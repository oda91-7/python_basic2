import random
from typing import List


def roll_dice_sided_n(side: int, times: int) -> List[int]:
    """N面サイコロをM回振った結果を返す"""
    results = []

    for _ in range(times):
        dice = random.randint(1, side)
        results.append(dice)

    return results


if __name__ == "__main__":
    n = int(input("サイコロの面の数は?: "))
    m = int(input("何回振りますか?: "))

    print(roll_dice_sided_n(side=n, times=m))

    # append = rist に追加する
    # split = 文字列型（String）オブジェクトを分割する為に使用するものです。 引数を省略した場合は空白で分割されます。 第一引数には区切り文字を指定することができます。