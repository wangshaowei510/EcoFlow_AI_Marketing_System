import pandas as pd


def analyze_trend(file):

    # 读取Google Trends数据
    data = pd.read_csv(
        file,
        skiprows=3,
        encoding="gb18030"
    )

    # 获取第二列搜索指数
    values = data.iloc[:, 1]

    # 转换成数字
    values = pd.to_numeric(
        values,
        errors="coerce"
    )

    # 计算平均值
    score = values.mean()

    return round(score, 2)



usa = analyze_trend(
    "am-multiTimeline (1).csv"
)


japan = analyze_trend(
    "ja-multiTimeline (2).csv"
)


germany = analyze_trend(
    "multiTimeline.csv"
)



print("================")
print("EcoFlow AI市场兴趣分析")
print("================")


print(
    "美国搜索热度:",
    usa
)


print(
    "日本搜索热度:",
    japan
)


print(
    "德国搜索热度:",
    germany
)