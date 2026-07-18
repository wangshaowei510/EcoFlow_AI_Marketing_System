import pandas as pd
import os


# =========================
# 1. 数据文件
# =========================

INPUT_FILE = "electronics_sample.csv"

OUTPUT_FILE = "ecoflow_reviews.csv"



# =========================
# 2. 储能相关关键词
# =========================

keywords = [

    # 品牌
    "ecoflow",
    "delta",
    "river",

    # 产品类别
    "power station",
    "portable power",
    "solar generator",
    "battery generator",

    # 电池
    "battery",
    "battery life",
    "capacity",
    "charging",

    # 电力
    "power",
    "watt",
    "wh",
    "energy",

    # 使用场景
    "camping",
    "outdoor",
    "rv",
    "emergency",
    "backup power",

    # 太阳能
    "solar",
    "solar panel"

]



# =========================
# 3. 加载数据
# =========================

print("======================")
print("EcoFlow 评论筛选系统")
print("======================")


if not os.path.exists(INPUT_FILE):

    print("找不到数据文件:")
    print(INPUT_FILE)

    exit()



data = pd.read_csv(
    INPUT_FILE,
    encoding="utf-8"
)



print("原始评论数量:")
print(len(data))



# =========================
# 4. 检查字段
# =========================


print("\n数据字段:")
print(data.columns)



# Amazon数据一般字段:

# reviewText
# summary
# overall



if "reviewText" not in data.columns:

    print("没有找到 reviewText 字段")

    exit()



# =========================
# 5. 数据清洗
# =========================


data = data.dropna(
    subset=["reviewText"]
)



# 转字符串

data["reviewText"] = (
    data["reviewText"]
    .astype(str)
    .str.lower()
)


if "summary" in data.columns:

    data["summary"] = (
        data["summary"]
        .fillna("")
        .astype(str)
        .str.lower()
    )

else:

    data["summary"] = ""




# 合并文本

data["text"] = (
    data["reviewText"]
    +
    " "
    +
    data["summary"]
)




# =========================
# 6. 筛选
# =========================


def match_keyword(text):

    for k in keywords:

        if k in text:

            return True

    return False



result = data[
    data["text"]
    .apply(match_keyword)
]



print("======================")

print("储能相关评论数量:")

print(len(result))


print("======================")



# =========================
# 7. 展示样例
# =========================


print("示例评论:")

print(
    result[
        [
            "overall",
            "summary",
            "reviewText"
        ]
    ]
    .head()
)



# =========================
# 8. 保存
# =========================


result.to_csv(

    OUTPUT_FILE,

    index=False,

    encoding="utf-8-sig"

)



print("======================")

print("完成!")

print("生成文件:")

print(OUTPUT_FILE)
