import streamlit as st

user_display_options = ["用户A", "用户B", "用户C"]

st.selectbox(
    "用户",
    user_display_options,
    key="selected_user",  # 唯一标识该组件的key
    label_visibility="collapsed"  # 隐藏标签，仅展示下拉框
)

st.write(f"当前选中的用户: {st.session_state.selected_user}")

if __name__ == '__main__':
    pass
