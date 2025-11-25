import streamlit as st
import pandas as pd

data = pd.DataFrame({
    "商品类别": ["电子产品", "服装", "食品", "电子产品", "服装", "食品"],
    "商品名称": ["手机", "T恤", "面包", "电脑", "裤子", "牛奶"],
    "价格": [5000, 199, 10, 8000, 299, 5]
})

st.subheader("交互控件案例")

# 下拉框
category = st.selectbox(
    "请选择商品类别",
    options=data["商品类别"].unique(),  # 下拉的唯一选项
    index=0  # 默认的第一个选项
)

# 滑块
price_range = st.slider(
    "请选择价格范围(元)",
    min_value=0,  # 最小值
    max_value=int(data["价格"].max()) + 1000,  # 最大值（加1000留余量）
    value=(0, 5000)  # 默认选择范围
)

# 多选框
selected_category = st.multiselect(
    "请选择商品名称（可选多个）",
    options=data[data["商品类别"] == category]["商品名称"].unique()  # 选项随下拉框类别变化
)

# 筛选数据
filtered_data1 = data[data["商品类别"] == category]

st.dataframe(filtered_data1)
if __name__ == '__main__':
    pass
