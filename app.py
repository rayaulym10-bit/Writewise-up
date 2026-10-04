import streamlit as st
import random

st.set_page_config(page_title="WriteWise IELTS", page_icon="🎓", layout="centered")

# --- ҰПАЙ ЖҮЙЕСІ ---
if "points" not in st.session_state:
    st.session_state.points = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "lesson" not in st.session_state:
    st.session_state.lesson = 1

st.title("🎓 WriteWise - IELTS Edition")
st.markdown(f"### 💰 Ұпайың: {st.session_state.points} | 🔥 Күн: {st.session_state.streak}")

# Күнделікті бонус
if st.button("🎁 Күнделікті бонус алу (+10 ұпай)"):
    st.session_state.points += 10
    st.session_state.streak += 1
    st.success("Бонус алдың! +10 ұпай!")
    st.balloons()

tab1, tab2, tab3 = st.tabs(["✍️ Эссе көмекшісі", "📚 IELTS 10 сөз", "🎮 Тест (+5 / -10)"])

# IELTS СӨЗДІКТЕРІ - ӘР САБАҚ 10 СӨЗ
ielts_lessons = {
    1: [
        {"en": "Analyse", "kz": "Талдау", "ex": "We need to analyse the data. - Біз деректерді талдауымыз керек."},
        {"en": "Significant", "kz": "Маңызды", "ex": "This is a significant result. - Бұл маңызды нәтиже."},
        {"en": "Consequently", "kz": "Салдарынан", "ex": "Consequently, prices rose. - Салдарынан баға өсті."},
        {"en": "Furthermore", "kz": "Сонымен қатар", "ex": "Furthermore, it is cheap. - Сонымен қатар ол арзан."},
        {"en": "Benefit", "kz": "Пайда", "ex": "The benefit of exercise. - Жаттығудың пайдасы."},
        {"en": "Environment", "kz": "Қоршаған орта", "ex": "Protect the environment. - Қоршаған ортаны қорға."},
        {"en": "Develop", "kz": "Дамыту", "ex": "Develop your skills. - Дағдыларыңды дамыт."},
        {"en": "Factor", "kz": "Фактор", "ex": "Key factor of success. - Жетістіктің негізгі факторы."},
        {"en": "Impact", "kz": "Әсер", "ex": "Positive impact. - Оң әсер."},
        {"en": "Research", "kz": "Зерттеу", "ex": "Recent research shows... - Соңғы зерттеулер көрсеткендей..."},
    ],
    2: [
        {"en": "Advantage", "kz": "Артықшылық", "ex": "The advantage of online learning. - Онлайн оқудың артықшылығы."},
        {"en": "Disadvantage", "kz": "Кемшілік", "ex": "One disadvantage is cost. - Бір кемшілігі - құны."},
        {"en": "Although", "kz": "Дегенмен", "ex": "Although it is hard, I will try. - Қиын болса да, тырысамын."},
        {"en": "Therefore", "kz": "Сондықтан", "ex": "Therefore, we must act. - Сондықтан әрекет етуіміз керек."},
        {"en": "Increase", "kz": "Арту", "ex": "Prices increased. - Бағалар артты."},
        {"en": "Decrease", "kz": "Азаю", "ex": "Crime decreased. - Қылмыс азайды."},
        {"en": "Governments", "kz": "Үкіметтер", "ex": "Governments should help. - Үкіметтер көмектесуі керек."},
        {"en": "Individual", "kz": "Жеке тұлға", "ex": "Individual responsibility. - Жеке жауапкершілік."},
        {"en": "Contribute", "kz": "Үлес қосу", "ex": "Contribute to society. - Қоғамға үлес қосу."},
        {"en": "Conclude", "kz": "Қорытындылау", "ex": "To conclude,... - Қорытындылай келе..."},
    ],
    3: [
        {"en": "Efficient", "kz": "Тиімді", "ex": "Efficient method. - Тиімді әдіс."},
        {"en": "Sustainable", "kz": "Тұрақты", "ex": "Sustainable development. - Тұрақты даму."},
        {"en": "Urbanization", "kz": "Урбанизация", "ex": "Urbanization is growing. - Урбанизация өсуде."},
        {"en": "Poverty", "kz": "Кедейлік", "ex": "Reduce poverty. - Кедейлікті азайту."},
        {"en": "Technology", "kz": "Технология", "ex": "Modern technology. - Заманауи технология."},
        {"en": "Education", "kz": "Білім", "ex": "Quality education. - Сапалы білім."},
        {"en": "Emphasize", "kz": "Атап өту", "ex": "I want to emphasize... - Атап өткім келеді..."},
        {"en": "Illustrate", "kz": "Суреттеу", "ex": "To illustrate this point... - Бұл ойды суреттеу үшін..."},
        {"en": "Perspective", "kz": "Көзқарас", "ex": "From my perspective... - Менің көзқарасым бойынша..."},
        {"en": "Acquire", "kz": "Игеру", "ex": "Acquire knowledge. - Білім игеру."},
    ]
}

with tab1:
    st.subheader("Эссеңді жаз, тексер!")
    text = st.text_area("Мәтін:", height=180, placeholder="IELTS эссеңді осында жаз...")
    if text:
        words = len(text.split())
        st.metric("Сөз саны", words)
        if words < 150:
            st.warning(f"IELTS үшін кем дегенде 250 сөз керек. Қазір {words} сөз.")
        else:
            st.success("✅ Тамаша! Сөз саны жеткілікті!")
            if st.button("Эссені тапсыру +20 ұпай"):
                st.session_state.points += 20
                st.balloons()
                st.success("+20 ұпай алдың!")

with tab2:
    st.subheader(f"📚 Сабақ {st.session_state.lesson}: 10 IELTS сөзі")

    lesson_words = ielts_lessons.get(st.session_state.lesson, ielts_lessons[1])

    for i, w in enumerate(lesson_words, 1):
        with st.expander(f"{i}. {w['en']} - {w['kz']}"):
            st.write(f"**Мысал:** {w['ex']}")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Сабақты үйрендім (+30 ұпай)"):
            st.session_state.points += 30
            st.success(f"Жарайсың! +30 ұпай! Келесі сабақ ашылды!")
            if st.session_state.lesson < 3:
                st.session_state.lesson += 1
    with col2:
        if st.button("Келесі сабақ ➡️"):
            if st.session_state.lesson < 3:
                st.session_state.lesson += 1
                st.rerun()

with tab3:
    st.subheader("🎮 IELTS Тест")
    st.caption("Дұрыс жауап: +5 ұпай | Қате: -10 ұпай")

    # Барлық сөздерден тест
    all_words = []
    for l in ielts_lessons.values():
        all_words.extend(l)

    if "current_q" not in st.session_state:
        st.session_state.current_q = random.choice(all_words)

    q = st.session_state.current_q
    st.markdown(f"### '{q['en']}' сөзінің мағынасы қандай?")

    # Жауап нұсқалары
    options = [q['kz']]
    while len(options) < 4:
        fake = random.choice(all_words)['kz']
        if fake not in options:
            options.append(fake)
    random.shuffle(options)

    choice = st.radio("Таңда:", options, key="quiz")

    if st.button("Жауап беру"):
        if choice == q['kz']:
            st.session_state.points += 5
            st.success(f"Дұрыс! +5 ұпай! 🔥 Қазір: {st.session_state.points}")
            st.balloons()
        else:
            st.session_state.points -= 10
            if st.session_state.points < 0:
                st.session_state.points = 0
            st.error(f"Қате! -10 ұпай. Дұрысы: {q['kz']}. Қазір: {st.session_state.points}")

        st.session_state.current_q = random.choice(all_words)
        st.rerun()

st.sidebar.markdown(f"## 🏆 {st.session_state.points} ұпай")
st.sidebar.write(f"Сабақ: {st.session_state.lesson}/3")
st.sidebar.progress(st.session_state.lesson/3)
st.sidebar.info("Күнде кіріп ойнап, ұпай жина!")
