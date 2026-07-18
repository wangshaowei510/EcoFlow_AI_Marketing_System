import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC']
plt.rcParams['axes.unicode_minus'] = False
import pandas as pd
from collections import Counter



def analyze_reviews(file):

    print("================")
    print("EcoFlow AI 用户评论分析")
    print("================")


    #读取数据
    data = pd.read_csv(
        file,
        encoding="utf-8"
    )


    #评论数量

    print("\n评论数量:")
    print(len(data))


    #平均评分

    score=data["overall"].mean()

    print("\n平均评分:")
    print(round(score,2))


    #好评比例

    good=len(
        data[data["overall"]>=4]
    )

    bad=len(
        data[data["overall"]<=2]
    )


    print("\n好评比例:")
    print(
        round(good/len(data)*100,2),
        "%"
    )


    print("\n差评比例:")
    print(
        round(bad/len(data)*100,2),
        "%"
    )



    #关键词分析

    keywords=[
        "battery",
        "power",
        "portable",
        "charging",
        "price",
        "weight",
        "quality"
    ]


    text=" ".join(
        data["reviewText"]
        .dropna()
        .astype(str)
        .tolist()
    ).lower()



    print("\n用户关注因素:")

    result={}

    for k in keywords:

        result[k]=text.count(k)


    for k,v in result.items():

        print(
            k,
            ":",
            v
        )



if __name__=="__main__":

    analyze_reviews(
        "electronics_sample.csv"
    )