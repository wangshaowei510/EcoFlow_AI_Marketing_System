import pandas as pd


def ad_optimizer(review_file):

    print("==============================")
    print("EcoFlow AI 广告智能优化系统")
    print("==============================")


    # 读取真实评论
    data = pd.read_csv(
        review_file,
        encoding="utf-8-sig"
    )


    print("\n评论数量:")
    print(len(data))


    # 关键词分析

    keywords = {
        "battery":0,
        "power":0,
        "portable":0,
        "charging":0,
        "price":0,
        "weight":0,
        "quality":0
    }


    for text in data["reviewText"].astype(str):

        text=text.lower()

        for k in keywords:

            if k in text:
                keywords[k]+=1



    print("\n用户关注因素:")

    for k,v in keywords.items():

        print(
            k,
            ":",
            v
        )


    # 排序

    sorted_keywords = sorted(
        keywords.items(),
        key=lambda x:x[1],
        reverse=True
    )


    top_factor = sorted_keywords[0][0]


    print("\n==============================")
    print("AI市场推荐")
    print("==============================")


    if top_factor in [
        "battery",
        "power"
    ]:

        market="德国"

        reason=(
            "德国消费者更加关注产品可靠性、"
            "续航能力以及长期使用价值"
        )


    elif top_factor=="portable":

        market="美国"

        reason=(
            "美国市场户外活动较多，"
            "便携能源需求明显"
        )


    else:

        market="日本"

        reason=(
            "日本消费者关注产品质量和使用体验"
        )



    print(
        "推荐重点市场:",
        market
    )

    print(
        "推荐原因:",
        reason
    )


    print("\n==============================")
    print("AI广告策略")
    print("==============================")


    print(
        """
核心广告主题:

Power Anywhere,
Reliable Energy Anytime


目标用户:

• Outdoor camping users
• Emergency backup users
• RV users


推荐渠道:

1. Amazon Sponsored Ads

2. Google Search Ads

3. Reddit Outdoor Communities


广告优化方向:

突出:

✓ Battery Life
✓ Fast Charging
✓ Portable Design
✓ Reliability

避免:

✗ 只强调低价格
✗ 单纯参数堆砌

"""
    )



if __name__=="__main__":


    ad_optimizer(
        "ecoflow_reviews.csv"
    )