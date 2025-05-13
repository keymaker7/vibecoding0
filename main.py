import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 탐험🌟",
    page_icon="🌈",
    layout="wide"
)

# 🎨 CSS로 폰트와 색상 스타일링
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    html, body, [class*="css"] {
        font-family: 'Jua', sans-serif;
        background-color: #fff8fc;
    }
    .job-card {
        background-color: #ffe4f0;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        font-size:18px;
        box-shadow: 2px 2px 5px #ccc;
        cursor: pointer;
    }
    .job-card:hover {
        background-color: #ffd6ec;
    }
    </style>
""", unsafe_allow_html=True)

# 직업 데이터
job_details = {
    "📷 사진작가": {
        "설명": "세상의 아름다운 순간을 사진으로 담는 예술가예요!",
        "관련학과": "사진영상학과, 디자인학부",
        "추천대학": "서울예대, 중앙대학교, 계원예대"
    },
    "🎭 배우": {
        "설명": "연기와 표현으로 사람들에게 감동을 주는 예술가예요!",
        "관련학과": "연극영화과, 공연예술학부",
        "추천대학": "한국예술종합학교, 동국대학교, 중앙대학교"
    },
    "👩‍🏫 선생님": {
        "설명": "아이들을 가르치고 함께 성장하는 교육 전문가예요!",
        "관련학과": "초등교육과, 유아교육과",
        "추천대학": "공주교육대학교, 진주교대, 이화여자대학교"
    },
    "🎨 디자이너": {
        "설명": "멋지고 창의적인 아이디어로 세상을 꾸미는 사람!",
        "관련학과": "시각디자인과, 산업디자인과",
        "추천대학": "홍익대학교, 국민대학교, 서울과학기술대학교"
    },
    # 필요한 만큼 추가 가능
}

# MBTI 선택
st.title("💫 MBTI로 알아보는 나의 미래 직업")
mbti_selected = st.selectbox("🧠 당신의 MBTI를 선택하세요!", ["ISFP", "ENFP", "INFP", "ESFP"])

# MBTI별 직업 (예시: ISFP)
mbti_jobs = {
    "ISFP": ["📷 사진작가", "🎨 디자이너"],
    "ENFP": ["🎭 배우", "🎨 디자이너"],
    "INFP": ["🎭 배우", "👩‍🏫 선생님"],
    "ESFP": ["🎭 배우", "📷 사진작가"]
}

# 직업 리스트 출력
st.subheader(f"🌟 [{mbti_selected}]에게 어울리는 직업 리스트")
cols = st.columns(2)
for i, job in enumerate(mbti_jobs[mbti_selected]):
    with cols[i % 2]:
        # 클릭 감지
        if st.button(job, key=job):
            with st.expander(f"🔍 {job}에 대해 알아보기!", expanded=True):
                st.write(f"📌 **설명**: {job_details[job]['설명']}")
                st.write(f"🎓 **관련 학과**: {job_details[job]['관련학과']}")
                st.write(f"🏫 **추천 대학**: {job_details[job]['추천대학']}")
