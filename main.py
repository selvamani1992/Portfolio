import streamlit as st
from streamlit_option_menu import option_menu
import pybase64
from streamlit_timeline import timeline
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Selvamani Andiappan",
                   page_icon="",
                   layout="wide",
                   initial_sidebar_state="expanded")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return pybase64.b64encode(data).decode()
img = get_img_as_base64("bg.jpg")
sideimg = get_img_as_base64("sbg.jpg")
dp = get_img_as_base64("dp.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{sideimg}");
background-position: 100%; 
background-repeat: repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='color: WHITE;'><b>SELVAMANI ANDIAPPAN</b></h1>", unsafe_allow_html=True)
#st.title('SELVAMANI ANDIAPPAN')

with st.sidebar:
    #st.image('dp.png',width=150)
    page = option_menu("",
                options=['Home','Projects','Contact'],
                default_index=0,
                orientation='vertical')
if page == "Home":
    st.markdown("<p style='color: white;'><b>Welcome to my professional portfolio, where a decade of diverse expertise "
                "converges with a proven track record of leadership and strategic prowess. "
                "With five years of dedicated experience as an Operations Manager, "
                "I've honed exceptional planning and problem-solving skills to elevate "
                "business strategies and daily operations. Profoundly attuned to industry trends, "
                "I possess an innate ability to identify opportunities for improvement and "
                "implement them with precision. Recently certified in Data Science, "
                "I'm now equipped with cutting-edge knowledge in data analysis, "
                "machine learning, and statistical modeling, enabling me to unlock "
                "the full potential of data for informed decision-making and strategic insights. "
                "As you explore my journey, you'll discover a commitment to continuous growth and "
                "a dedication to driving results, both in the realm of operations management and "
                "the exciting world of data science </b></p><br>",unsafe_allow_html=True)

    st.markdown("<h3 style='color: white;'><b>WORK EXPERIENCE:</b></h3>", unsafe_allow_html=True)


    with st.spinner(text="Building line"):
        with open('work_timeline.json', "r") as f:
            data = f.read()
            timeline(data, height=500)

    st.markdown("<h3 style='color: white;'><b>EDUCATION:</b></h3>", unsafe_allow_html=True)
    st.markdown(
        "#### <font color='#6e6e6e'>"
        "&nbsp;&nbsp;&nbsp;IITM Advance Professional Programing with Master Data Science,<br> "
        "**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Guvi - IIT Madras](https://www.guvi.in/)**<br> "
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Feb, 2023 - Jul, 2023)</font>",
        unsafe_allow_html=True)
    st.markdown(
        "#### <font color='#6e6e6e'>"
        "&nbsp;&nbsp;&nbsp;Bachelor of Computer Application,<br> "
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**[Jairam Arts & Science College](https://jairaminfo.in/)**<br> "
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Jun, 2009 - Apr, 2012)</font>",
        unsafe_allow_html=True)

elif page == "Projects":
    st.markdown("<h3 style='color: #0a1828;'><b>Docx Translator:</b></h3>", unsafe_allow_html=True)
    st.markdown("""<p style='color: #0a1828;'>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- This feature will assist users in translating content in the docx format from one language to another. It also includes automatic name localization based on the user's selected region.
                </P""", unsafe_allow_html=True)
    mention(label="Streamlit App", icon="streamlit",
            url="https://doctranslator-selvamaniind.streamlit.app/", )
    mention(label="Github Repo", icon="github", url="https://github.com/selvamani1992/DocTranslator", )

    st.markdown("<h3 style='color: #0a1828;'><b><br>Loan Approval Prediction:</b></h3>", unsafe_allow_html=True)
    #st.markdown("<h4 style='color: #0a1828;'><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EDUCATION:</b></h4>", unsafe_allow_html=True)
    st.markdown("""<p style='color: #0a1828;'>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- With the assistance of this machine learning model, we can assess an individual's eligibility for obtaining a loan. By analyzing multiple parameters, this model possesses the capability to deliver accurate predictions and promote fair lending practices.
                </P""", unsafe_allow_html=True)
    #mention(label="Streamlit App", icon="streamlit", url="https://doctranslator-selvamaniind.streamlit.app/", )
    mention(label="Github Repo", icon="github", url="https://github.com/selvamani1992/Loan_Approval_Prediction" )