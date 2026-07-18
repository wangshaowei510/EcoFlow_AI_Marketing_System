import pandas as pd


def analyze_user_journey(question):

    question = question.lower()


    # 用户阶段判断

    if any(word in question for word in [
        "多少钱",
        "价格",
        "优惠",
        "购买",
        "在哪里买"
    ]):
        stage = "购买决策阶段"


    elif any(word in question for word in [
        "怎么样",
        "好吗",
        "区别",
        "比较",
        "容量"
    ]):
        stage = "产品考虑阶段"


    elif any(word in question for word in [
        "是什么",
        "介绍",
        "了解"
    ]):
        stage = "兴趣了解阶段"


    else:
        stage = "需求探索阶段"



    # 场景分析

    if any(word in question for word in [
        "冰箱",
        "停电",
        "家庭"
    ]):

        scene = "家庭备用电源场景"

        answer = """
推荐产品：

EcoFlow DELTA 2 Max


分析：

产品容量：
2048Wh


如果冰箱功率约120W：

理论运行时间：

2048 ÷ 120 ≈ 17小时


适合：

家庭停电备用
长期能源保障
        """


    elif any(word in question for word in [
        "露营",
        "户外",
        "旅行"
    ]):

        scene = "户外移动能源场景"

        answer = """
推荐产品：

EcoFlow RIVER系列


分析：

适合：

户外旅行
露营活动
移动供电需求
        """


    elif any(word in question for word in [
        "太阳能",
        "solar"
    ]):

        scene = "太阳能能源管理场景"

        answer = """
推荐产品：

EcoFlow DELTA系列


分析：

结合太阳能板：

提高绿色能源利用效率。
        """


    else:

        scene = "通用能源需求"

        answer = """
AI建议：

根据您的需求，
推荐进一步了解EcoFlow产品组合。
        """



    return {

        "用户阶段": stage,

        "使用场景": scene,

        "AI推荐": answer

    }