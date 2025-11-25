import streamlit as st

st.sidebar.title("侧边栏控件")
name = st.sidebar.text_input("输入你的名字")
age = st.sidebar.number_input("请输入你的年龄", min_value=0, max_value=120)

col1, col2 = st.columns(2)

with col1:
    st.subheader("个人信息")
    st.write(f"姓名：{name}")
    st.write(f"年龄：{age}")

with col2:
    st.subheader("提示：")
    if age < 18:
        st.warning("请勿below18岁")
    else:
        st.info("正常使用  ")

with st.expander("查看说明书"):
    st.write("1。dfadfasf")
    st.write("2。dfadfasf")
    st.write("3。dfadfasf")

if __name__ == '__main__':
    pass
