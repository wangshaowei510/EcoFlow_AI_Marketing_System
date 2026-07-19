# user_journey.py

def analyze_user_journey(question):

    question = question.lower()


    # =========================
    # 1. 用户购买阶段判断
    # =========================

    if any(word in question for word in [
        "多少钱",
        "价格",
        "优惠",
        "购买",
        "在哪里买",
        "下单",
        "怎么买"
    ]):
        stage = "购买决策阶段"


    elif any(word in question for word in [
        "怎么样",
        "好吗",
        "区别",
        "比较",
        "容量",
        "性能",
        "评价"
    ]):
        stage = "产品考虑阶段"


    elif any(word in question for word in [
        "是什么",
        "介绍",
        "了解",
        "功能"
    ]):
        stage = "兴趣了解阶段"


    else:
        stage = "需求探索阶段"



    # =========================
    # 2. 使用场景分析
    # =========================


    if any(word in question for word in [
        "冰箱",
        "停电",
        "家庭",
        "备用",
        "应急"
    ]):

        scene = "家庭备用电源场景"


        product = {
            "name":"EcoFlow DELTA 2 Max",
            "capacity":"2048Wh",
            "power":"2400W",
            "reason":
            "适合家庭停电备用，可支持冰箱、照明、路由器等家庭设备供电。"
        }



    elif any(word in question for word in [
        "露营",
        "户外",
        "旅行",
        "房车",
        "野外"
    ]):

        scene = "户外移动能源场景"


        product = {
            "name":"EcoFlow RIVER 2 Pro",
            "capacity":"768Wh",
            "power":"800W",
            "reason":
            "产品体积小、便携性强，适合露营、旅行和户外移动供电需求。"
        }



    elif any(word in question for word in [
        "太阳能",
        "solar",
        "光伏"
    ]):

        scene = "太阳能能源管理场景"


        product = {
            "name":"EcoFlow DELTA Pro",
            "capacity":"3600Wh",
            "power":"3600W",
            "reason":
            "支持太阳能输入，适合长期能源管理和家庭储能应用。"
        }



    else:

        scene = "综合能源需求场景"


        product = {
            "name":"EcoFlow系列产品",
            "capacity":"根据需求匹配",
            "power":"根据使用场景匹配",
            "reason":
            "建议进一步了解不同容量产品组合。"
        }



    # =========================
    # 3. 生成AI推荐结果
    # =========================


    answer = f"""
推荐产品：
{product['name']}


核心参数：
容量：{product['capacity']}
输出功率：{product['power']}


推荐理由：
{product['reason']}


营销建议：
针对该用户需求，
突出产品可靠性、续航能力以及使用场景匹配优势。
"""

    return {

        "用户阶段":stage,

        "使用场景":scene,

        "AI推荐":answer

    }



# =========================
# 测试运行
# =========================

if __name__ == "__main__":


    result = analyze_user_journey(
        "家庭停电，需要给冰箱供电"
    )


    print("===================")
    print("EcoFlow AI用户旅程分析")
    print("===================")

    print("==============================")
    print("EcoFlow AI 用户旅程分析系统")
    print("==============================")


    print()

    print("用户需求：")
    print("家庭停电，需要冰箱供电")


    print()

    print("用户阶段：")
    print(result["用户阶段"])


    print()

    print("使用场景：")
    print(result["使用场景"])


    print()
    print("==============================")
    print("AI个性化推荐")
    print("==============================")


    print()

    print(result["AI推荐"])

    print("==============================")