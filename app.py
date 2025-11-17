import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="포트폴리오",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 스타일
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .profile-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .project-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }
    .project-card:hover {
        transform: translateY(-5px);
    }
    .skill-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        margin: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        font-size: 0.9rem;
    }
    .contact-button {
        padding: 0.75rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        font-size: 1rem;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# 홈 섹션
def show_home():
    st.markdown('<div class="section-title">👋 안녕하세요!</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="profile-card">
            <h2 style="text-align: center; color: #667eea;">개발자 포트폴리오</h2>
            <p style="text-align: center; font-size: 1.2rem; color: #666;">
                열정적인 개발자로서 성장하고 있습니다.<br>
                사용자 경험을 중시하며, 깔끔하고 효율적인 코드를 작성합니다.
            </p>
        </div>
        """, unsafe_allow_html=True)

# 프로젝트 섹션
def show_projects():
    st.markdown('<div class="section-title">🚀 프로젝트</div>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "웹 애플리케이션 프로젝트",
            "description": "현대적인 웹 기술을 활용한 반응형 웹 애플리케이션",
            "tech": ["Python", "Streamlit", "React"],
            "status": "완료"
        },
        {
            "title": "데이터 분석 대시보드",
            "description": "실시간 데이터 시각화 및 분석 대시보드",
            "tech": ["Python", "Pandas", "Plotly"],
            "status": "진행중"
        },
        {
            "title": "머신러닝 프로젝트",
            "description": "예측 모델 개발 및 최적화",
            "tech": ["Python", "Scikit-learn", "TensorFlow"],
            "status": "완료"
        }
    ]
    
    for project in projects:
        tech_tags = " ".join([f'<span class="skill-badge">{tech}</span>' for tech in project["tech"]])
        st.markdown(f"""
        <div class="project-card">
            <h3 style="color: #667eea;">{project["title"]}</h3>
            <p style="color: #666;">{project["description"]}</p>
            <div style="margin-top: 1rem;">
                {tech_tags}
            </div>
            <p style="margin-top: 1rem; color: #999; font-size: 0.9rem;">상태: {project["status"]}</p>
        </div>
        """, unsafe_allow_html=True)

# 기술 스택 섹션
def show_skills():
    st.markdown('<div class="section-title">💻 기술 스택</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="profile-card">
            <h3 style="color: #667eea; text-align: center;">프론트엔드</h3>
            <div style="text-align: center; padding: 1rem;">
                <span class="skill-badge">HTML/CSS</span><br>
                <span class="skill-badge">JavaScript</span><br>
                <span class="skill-badge">React</span><br>
                <span class="skill-badge">Streamlit</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="profile-card">
            <h3 style="color: #667eea; text-align: center;">백엔드</h3>
            <div style="text-align: center; padding: 1rem;">
                <span class="skill-badge">Python</span><br>
                <span class="skill-badge">Django</span><br>
                <span class="skill-badge">Flask</span><br>
                <span class="skill-badge">Node.js</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="profile-card">
            <h3 style="color: #667eea; text-align: center;">기타</h3>
            <div style="text-align: center; padding: 1rem;">
                <span class="skill-badge">Git</span><br>
                <span class="skill-badge">Docker</span><br>
                <span class="skill-badge">AWS</span><br>
                <span class="skill-badge">SQL</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 연락처 섹션
def show_contact():
    st.markdown('<div class="section-title">📧 연락처</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="profile-card">
            <div style="text-align: center;">
                <h3 style="color: #667eea;">함께 일하고 싶으신가요?</h3>
                <p style="color: #666; font-size: 1.1rem; margin: 1.5rem 0;">
                    프로젝트나 협업에 관심이 있으시다면 언제든지 연락주세요!
                </p>
                <div style="margin-top: 2rem;">
                    <p style="color: #666;">📧 Email: your.email@example.com</p>
                    <p style="color: #666;">💼 GitHub: github.com/yourusername</p>
                    <p style="color: #666;">🌐 LinkedIn: linkedin.com/in/yourprofile</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 사이드바 네비게이션
st.sidebar.title("🧭 네비게이션")
page = st.sidebar.radio("페이지 선택", ["홈", "프로젝트", "기술 스택", "연락처"])

# 페이지 라우팅
if page == "홈":
    show_home()
elif page == "프로젝트":
    show_projects()
elif page == "기술 스택":
    show_skills()
elif page == "연락처":
    show_contact()

# 푸터
st.markdown("""
<div style="text-align: center; padding: 2rem; color: white;">
    <p>© 2024 포트폴리오. Made with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)

