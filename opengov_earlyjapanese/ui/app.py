import streamlit as st
from opengov_earlyjapanese.core.hiragana import HiraganaTeacher

st.set_page_config(page_title="OpenGov Early Japanese")
st.title("OpenGov Early Japanese")

st.subheader("Hiragana Lesson")
row = st.selectbox(
    "Row",
    [
        "a_row",
        "ka_row",
        "sa_row",
        "ta_row",
        "na_row",
        "ha_row",
        "ma_row",
        "ya_row",
        "ra_row",
        "wa_row",
    ],
)
t = HiraganaTeacher()
lesson = t.get_lesson(row)
st.write("Characters:", " ".join(lesson.characters))
with st.expander("Mnemonics"):
    for ch, m in lesson.mnemonics.items():
        st.markdown(f"**{ch}**: {m}")
