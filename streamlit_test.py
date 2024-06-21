# steamlit 라이브러리 설치 후 시작함
# 실행하기 위해서는 새 터미널을 만들어서 아래애 streamlit run streamlit.py 해준다

import streamlit as st
from PIL import Image
import exchange_rate

# st.title("안녕하세요.")
# st.header("당각현")

st.sidebar.header("로그인")
user_id = st.sidebar.text_input("아이디 입력", value = '', max_chars=15)
user_pw = st.sidebar.text_input("비밀번호 입력", value = '', type='password')

if user_id == 'gakhyun' and user_pw == '1234':
    st.sidebar.header("Gakhyun's World")
    # sel_options = ['','진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '생명의 나무', '월하정인']
    # user_opt = st.sidebar.selectbox("좋아하는 작품은?", sel_options, index=0)
    # st.sidebar.write("**선택한 그림은**", user_opt)

    menu = st.sidebar.radio("메뉴 선택", ['환율 조회', '부동산 조회(EDA)', '인공지능 예측/분류'], index=None)

    if menu == '환율 조회':
        exchange_rate.exchange_main()
        st.sidebar.write("환율 조회")
    elif menu == '부동산 조회(EDA)':
        st.sidebar.write("부동산 조회(EDA)")
    elif menu == '인공지능 예측/분류':
        st.sidebar.write("인공지능 예측/분류")
    else:
        st.sidebar.write("당신의 선택은?")
    
    # 메인 화면
