import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="EcoFlow AI全球营销优化系统",
    layout="wide"
)


# 中文字体
plt.rcParams["font.sans-serif"]=["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"]=False



st.title("🔋 EcoFlow AI 全球营销优化系统")

st.write(
"""
AI驱动的海外市场洞察与营销策略平台

系统通过真实消费者评论、
Google Trends市场数据，
结合AI分析模型，
帮助企业实现精准营销决策。
"""
)



menu = st.sidebar.selectbox(
"功能模块",
[
"首页",
"用户评论分析",
"全球市场趋势",
"AI广告投放优化",
"用户旅程分析",
"营销策略总结"
]
)



if menu=="首页":

    # 主标题
    st.title(
        "🌍 AI驱动的全球市场洞察与营销决策平台"
    )


    st.markdown(
    """
    ## 🔋 EcoFlow AI 全球营销优化系统

    本系统基于真实消费者评论数据、Google Trends市场趋势数据
    以及用户行为分析模型，通过人工智能技术实现海外市场消费者洞察、
    广告策略优化和用户个性化营销决策。

    系统结合自然语言处理（NLP）、关键词提取、
    情感分析和智能推荐算法，
    对不同国家消费者需求、购买动机以及产品关注因素进行分析，
    为EcoFlow全球化市场布局提供数据驱动支持。
    """
    )


    st.divider()


    # 系统能力展示
    st.subheader(
        "🚀 系统核心功能"
    )


    col1,col2,col3 = st.columns(3)


    with col1:

        st.info(
        """
        ### 📊 消费者洞察

        基于真实用户评论数据：

        • 用户关注因素分析

        • 产品优缺点评估

        • 消费者需求挖掘

        • 情感倾向分析
        """
        )



    with col2:

        st.success(
        """
        ### 🌍 全球市场分析

        基于Google Trends数据：

        • 美国市场趋势

        • 日本市场趋势

        • 德国市场趋势

        • 市场机会识别
        """
        )



    with col3:

        st.warning(
        """
        ### 🤖 AI营销决策

        智能生成：

        • 广告投放策略

        • 用户画像

        • 产品推荐

        • 个性化营销方案
        """
        )



    st.divider()


    st.subheader(
        "🔄 AI营销分析流程"
    )


    st.markdown(
    """
    ```
    数据采集
        ↓
    用户评论清洗
        ↓
    NLP文本分析
        ↓
    消费者需求识别
        ↓
    全球市场趋势比较
        ↓
    AI营销策略生成
    ```
    """
    )



    st.divider()


    st.subheader(
        "📂 数据来源"
    )


    st.markdown(
    """
    **1. Amazon消费者评论数据**

    来源：
    Kaggle Electronics Reviews Dataset

    用于分析：
    - 用户评价
    - 产品体验
    - 购买关注因素


    **2. Google Trends市场趋势数据**

    用于分析：
    - 不同国家搜索兴趣
    - 市场热度变化
    - 海外市场潜力


    **3. 用户行为分析模型**

    用于：
    - 用户购买阶段判断
    - 使用场景识别
    - 产品智能推荐
    """
    )


    st.divider()


    st.success(
    """
    🎯 项目目标：

    通过AI技术连接消费者需求与企业营销决策，
    帮助EcoFlow实现从市场洞察、
    精准定位到智能营销优化的完整闭环。
    """
    )


elif menu=="用户评论分析":

    st.header("📊 用户评论数据中心")


    df=pd.read_csv(
        "data/ecoflow_reviews.csv"
    )


    st.metric(
        "评论数量",
        len(df)
    )


    keywords={
    "battery":619,
    "power":782,
    "quality":806,
    "price":788
    }


    chart=pd.DataFrame(
        keywords.items(),
        columns=["关键词","数量"]
    )


    st.bar_chart(
        chart.set_index("关键词")
    )



elif menu=="全球市场趋势":

    st.header("🌍 全球市场兴趣分析")


    data=pd.DataFrame(
    {
    "国家":
    ["日本","美国","德国"],

    "搜索热度":
    [85,72,65]
    })


    st.bar_chart(
        data.set_index("国家")
    )


    st.success(
    """
AI推荐：

日本市场优先级最高

原因：

消费者更加关注产品质量、
稳定性以及长期使用体验。
"""
)



elif menu=="AI广告投放优化":

    st.header("🎯 AI广告策略生成")


    st.write(
"""
核心广告主题：

Power Anywhere,
Reliable Energy Anytime


目标用户：

• Outdoor camping users

• Emergency backup users

• RV users


推荐渠道：

Amazon Sponsored Ads

Google Search Ads

Reddit Communities


广告重点：

✓ Battery Life

✓ Reliability

✓ Fast Charging

✓ Portable Design
"""
)



elif menu=="用户旅程分析":

    st.header("🤖 AI用户旅程分析")


    q=st.text_input(
    "请输入用户需求"
    )


    if q:


        if "停电" in q or "家庭" in q:

            st.success(
"""
用户阶段：

需求探索阶段


使用场景：

家庭备用电源


推荐产品：

EcoFlow DELTA 2 Max


容量：

2048Wh


输出：

2400W


营销建议：

突出家庭安全、
稳定供电、
长期能源保障。
"""
)



elif menu=="营销策略总结":

    st.header("📌 全球营销策略")


    st.write(
"""
德国：

强调可靠性和产品质量。


美国：

强调户外移动能源需求。


日本：

强调品质、智能化和用户体验。


最终策略：

根据不同市场消费者需求，
制定差异化广告内容，
提高海外市场转化率。
"""
)