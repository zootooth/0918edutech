import streamlit as st
import numpy as np

st.title('Streamlit 요소 데모')

st.header('1. 텍스트와 마크다운')
st.write('이것은 일반 텍스트입니다.')
st.markdown('**마크다운** _스타일링_도 지원합니다!')

st.header('2. 입력 위젯')
name = st.text_input('이름을 입력하세요:')
age = st.number_input('나이를 입력하세요:', min_value=0, max_value=120, value=25)
agree = st.checkbox('동의합니다')

st.header('3. 버튼')
if st.button('클릭하세요!'):
    st.success('버튼이 클릭되었습니다!')

st.header('4. 슬라이더')
value = st.slider('값을 선택하세요', 0, 100, 50)
st.write(f'선택한 값: {value}')

st.header('5. 선택 위젯')
color = st.selectbox('좋아하는 색상은?', ['빨강', '초록', '파랑'])
st.write(f'선택한 색상: {color}')

st.header('6. 데이터프레임과 차트')
df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)
st.dataframe(df)
st.line_chart(df)

st.header('7. 파일 업로드')
uploaded_file = st.file_uploader('CSV 파일을 업로드하세요', type='csv')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write('업로드된 데이터:')
    st.dataframe(data)
