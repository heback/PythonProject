import streamlit as st

def main():
    st.title("Streamlit 테스트 페이지")
    st.write("이 페이지는 Streamlit 기능을 테스트하기 위해 만들어졌습니다.")

    # 텍스트 입력
    name = st.text_input("이름을 입력하세요:")
    if name:
        st.success(f"안녕하세요, {name}님!")

    # 숫자 입력
    number = st.number_input("좋아하는 숫자를 입력하세요:", min_value=0, max_value=100, value=10)
    st.write(f"입력한 숫자: {number}")

    # 버튼
    if st.button("버튼 클릭"):
        st.write("버튼이 클릭되었습니다!")

    # 체크박스
    if st.checkbox("체크박스를 선택하세요"):
        st.write("체크박스가 선택되었습니다!")

    # 슬라이더
    slider_val = st.slider("값을 선택하세요", 0, 50, 25)
    st.write(f"선택한 값: {slider_val}")

    # 파일 업로드
    uploaded_file = st.file_uploader("파일을 업로드하세요")
    if uploaded_file:
        st.write("파일 이름:", uploaded_file.name)


    st.info("파일이 변경되면 자동으로 반영됩니다.")

if __name__ == "__main__":
    main()
