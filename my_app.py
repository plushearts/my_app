import streamlit as st


def app():
    st.title('MY APP')
    st.markdown('———————————————————————')
    st.markdown('*日常数据表，最近维护时间*：**2024-12-03**')
    st.markdown('*登录数据表，最近维护时间*：**2024-12-01**')
    st.markdown('*企微数据表，最近维护时间*：**2024-11-27**')
    st.markdown('========================================')

def example():
    if st.checkbox("Use url", value=True):
        add_logo("http://placekitten.com/120/120")
    else:
        add_logo("gallery/kitty.jpeg", height=300)
    st.write("👈 Check out the cat in the nav-bar!")


if __name__ == '__main__':
    app()
    example()
