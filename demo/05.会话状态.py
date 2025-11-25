import streamlit as st

st.subheader("会话状态")

if "num" not in st.session_state:
    st.session_state.num = 0

if st.button("点击+1"):
    st.session_state.num += 1

if st.button("点击-1"):
    st.session_state.num -= 1

st.write(f"当前计数为: {st.session_state.num}")

if __name__ == '__main__':
    pass
