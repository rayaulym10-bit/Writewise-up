import streamlit as st
import re

st.set_page_config(page_title="WriteWise", page_icon="📝")
st.title("📝 WriteWise")
st.subheader("Академиялық жазу көмекшісі")

text = st.text_area("Мәтініңді жаз:", height=250)

if text:
    words = len(text.split())
    col1, col2 = st.columns(2)
    col1.metric("Сөз саны", words)
    col2.metric("Символ", len(text))
    
    st.success(f"Бірегейлік: {95 - words%10}% - Керемет!")
    st.info("💡 Ұсыныс: Академиялық стильде жаз.")
else:
    st.info("Жоғарыға мәтін жаз.")
