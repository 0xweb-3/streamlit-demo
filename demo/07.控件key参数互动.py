import streamlit as st
import pandas as pd

data = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 35],
    "工资": [8000, 12000, 15000]
})

st.selectbox(
    "选择用户",
    data["姓名"].unique(),
    key="selected_user"
)

st.slider(
    "选择年龄范围",
    20, 40, (22, 35),
    key="age_range"
)

filtered_data = data[
    (data["姓名"] == st.session_state["selected_user"]) &
    (data["年龄"] >= st.session_state["age_range"][0]) &
    (data["年龄"] <= st.session_state["age_range"][1])
]

st.dataframe(filtered_data)


if __name__ == '__main__':
    pass