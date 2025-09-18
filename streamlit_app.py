import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("함수 그래프 그리기 앱")

# 함수 입력 받기
func_str = st.text_input("함수를 입력하세요 (예: np.sin(x), x**2, np.exp(x))", "np.sin(x)")

# x 범위 설정
x = np.linspace(-10, 10, 400)

try:
    # 입력된 함수 문자열을 실제 함수로 변환
    y = eval(func_str)
    # 그래프 그리기
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"y = {func_str}")
    st.pyplot(fig)
except Exception as e:
    st.error(f"그래프를 그릴 수 없습니다: {e}")
    
