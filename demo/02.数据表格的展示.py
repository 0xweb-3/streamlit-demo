import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.subheader("数据表格展示")

data = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 35],
    "工资": [8000, 12000, 15000]
})

st.dataframe(data, use_container_width=True)

st.subheader("数据图表展示")
plt.rcParams["font.family"] = ["sans-serif"]
plt.rcParams["font.sans-serif"] = ["SimHei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots()

ax.bar(data["姓名"], data["工资"], color="#1f77b4")
ax.set_xlabel("姓名")
ax.set_ylabel("工资(元)")
ax.set_title("员工工资分布")

st.pyplot(fig)

if __name__ == '__main__':
    pass
