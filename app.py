import streamlit as st
import random

st.title("확률 버튼 게임")

st.write("버튼을 누르면 확률에 따라 보상이 결정돼")

# 결과 저장용
if "total" not in st.session_state:
    st.session_state.total = 0

st.write(f"현재 점수: {st.session_state.total}")

col1, col2, col3 = st.columns(3)

# A 버튼
with col1:
    if st.button("A 버튼"):
        result = random.choice([4, 0])
        st.session_state.total += result
        st.write(f"A 결과: {result}")

# B 버튼
with col2:
    if st.button("B 버튼"):
        result = random.choice([5, 1, 0])
        st.session_state.total += result
        st.write(f"B 결과: {result}")

# C 버튼
with col3:
    if st.button("C 버튼"):
        result = random.choice([8, 3, -1, -2])
        st.session_state.total += result
        st.write(f"C 결과: {result}")

# 리셋 버튼
if st.button("점수 초기화"):
    st.session_state.total = 0
