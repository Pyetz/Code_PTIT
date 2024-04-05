import streamlit as st

def main():
    st.title("Factorial Calculator")
    string = st.text_input("Hãy nhập gì đó:")
    number = st.number_input("Hãy chọn con số mà bạn yêu thích trong khoảng 0->99:", min_value=0, max_value=99)
    if st.button("Thực hiện dự đoán"):
        st.write("Bạn chính là Bẻo Chum du côn ba trợn đúng hong muhahaha<3")
        #hiển thị thông báo
        st.balloons()

if __name__ == "__main__":
    main()
