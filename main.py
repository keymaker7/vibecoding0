import streamlit as st

# 🎨 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 진로 추천 🎯",
    page_icon="✨",
    layout="wide",
)

# 🎆 타이틀
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>💫 MBTI로 알아보는 ✨ 나의 미래 직업 💼</h1>", unsafe_allow_html=True)
st.markdown("### 🌈 아래에서 자신의 MBTI를 선택하면, 잘 어울리는 직업을 추천해드려요!")

# 🧠 MBTI 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["🔬 과학자", "💻 데이터 과학자", "🧠 전략 컨설턴트"],
    "INTP": ["🧪 연구원", "💡 발명가", "👨‍💻 소프트웨어 개발자"],
    "ENTJ": ["💼 CEO", "📊 경영 컨설턴트", "⚖️ 법률가"],
    "ENTP": ["🎙️ 방송인", "💭 스타트업 창업자", "🧑‍🚀 혁신가"],
    "INFJ": ["📚 작가", "🎨 예술가", "🤝 심리상담사"],
    "INFP": ["✍️ 시인", "🎼 작곡가", "🌍 NGO 활동가"],
    "ENFJ": ["👨‍🏫 선생님", "🎤 연설가", "💖 코치"],
    "ENFP": ["🌟 배우", "📚 콘텐츠 크리에이터", "🧳 여행 블로거"],
    "ISTJ": ["📊 회계사", "🏛️ 공무원", "🔧 기술자"],
    "ISFJ": ["👩‍⚕️ 간호사", "📦 사서", "👩‍🍳 제과제빵사"],
    "ESTJ": ["📈 관리자", "🏦 은행원", "👨‍✈️ 군인"],
    "ESFJ": ["💬 상담사", "🧑‍🏫 교사", "🎉 이벤트 플래너"],
    "ISTP": ["🔧 정비사", "🚘 자동차 디자이너", "🛠️ 기계 엔지니어"],
    "ISFP": ["📷 사진작가", "🎨 디자이너", "🎵 음악가"],
    "ESTP": ["💰 영업사원", "🛍️ 마케팅 전문가", "🎮 게임 스트리머"],
    "ESFP": ["🎭 배우", "🕺 엔터테이너", "🎤 가수"],
}

# 🎯 사용자 MBTI 선택
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요!", mbti_list)

# 💫 추천 결과
if selected_mbti:
    st.markdown(f"### 🧭 <span style='color:#4B0082'>[{selected_mbti}]</span> 유형에게 어울리는 직업은?", unsafe_allow_html=True)
    st.success("🌟 " + " | ".join(mbti_jobs[selected_mbti]))

# 🌈 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>✨ 만든이: 당신의 진로를 응원하는 AI ✨</p>", unsafe_allow_html=True)
