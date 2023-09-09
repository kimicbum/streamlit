import streamlit as st
st.title('새 탭 만들기!')

image_path='Faker_2020_interview.jpg'

st.image(image_path)

mbti = st.radio(
    '이 분은 누구입니까?',
    ('T슼', '3대떡', '페이커'))

if mbti == 'T슼':
    st.write('틀렸습니다')
elif mbti == '3대떡':
    st.write('ㅌㄽㄴㄷ')
else:
    st.write("정답")

 import streamlit as st
import pandas as pd

st.title('streamlit dataframe🎨')
dataframe = pd.DataFrame({
     'first column': [1, 2, 3, 4],
      'second column': [10, 20, 30, 40],
 })

 st.dataframe(dataframe, use_container_width=False)
 st.table(dataframe)

st.metric(label="온도", value="10℃", delta="1.2℃")
st.metric(label="삼성전자", value="61,00원", delta="-1,200원")

col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,228원", delta="-12.00원")
col2.metric(label="일본JPY(100엔)", value="958.63원", delta="-7.44원")
col3.metric(label="유럽연합EUR", value="1,335.82원", delta="11.44원")

