import streamlit as st
from streamlit_option_menu import option_menu
import pybase64
from streamlit_timeline import timeline
import streamlit.components.v1 as components
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
        "&nbsp;&nbsp;&nbsp;IIT-Madras Advance Professional Programing with Master Data Science,<br> "
        "**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Guvi - IIT Madras](https://www.guvi.in/)**<br> "
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Feb, 2023 - Jul, 2023)</font>",
        unsafe_allow_html=True)
    st.markdown(
        "#### <font color='#6e6e6e'>"
        "&nbsp;&nbsp;&nbsp;Bachelor of Computer Application,<br> "
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**[Jairam Arts & Science College](https://jairaminfo.in/)**<br><br> "
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Jun, 2009 - Apr, 2012)</font>",
        unsafe_allow_html=True)

    st.markdown("<h3 style='color: white;'><b>CERTIFICATIONS:</b></h3>", unsafe_allow_html=True)
    st.markdown("#### <font color='#6e6e6e'>"
        "&nbsp;&nbsp;&nbsp;- **[Python from IIT-Madras](https://digitalskills.pravartak.org.in/verify/cert/275552db0a2962c317ed0532f6366ac5)**<br>"
                "</font>",
        unsafe_allow_html=True)
    st.markdown("#### <font color='#6e6e6e'>"
                "&nbsp;&nbsp;&nbsp;- **[Professional in Advanced Programming from IIT-Madras](https://digitalskills.pravartak.org.in/verify/cert/b3b1b5c4d9eaf0772914813eea65f66a)**<br></font>",
                unsafe_allow_html=True)
    st.markdown("#### <font color='#6e6e6e'>"
                "&nbsp;&nbsp;&nbsp;- **[Master Data Science from Guvi](www.guvi.in/verify-certificate?id=50116pLo53c82mJUT9)**<br></font>",
                unsafe_allow_html=True)
    st.markdown("#### <font color='#6e6e6e'>"
                "&nbsp;&nbsp;&nbsp;- **[Machine Learning from Guvi](https://www.guvi.in/verify-certificate?id=13Qax66108sVj29889)**<br></font>",
                unsafe_allow_html=True)
    st.markdown("#### <font color='#6e6e6e'>"
                "&nbsp;&nbsp;&nbsp;- **[MongoDB from Guvi](https://www.guvi.in/verify-certificate?id=131G3Vx9w14n68k4TK)**<br></font>",
                unsafe_allow_html=True)
    st.markdown("#### <font color='#6e6e6e'>"
                "&nbsp;&nbsp;&nbsp;- **[PowerBI from Guvi](https://www.guvi.in/verify-certificate?id=9Uo53d551J27Nsr608&course=powerbi_step_by_step_english)**<br></font>",
                unsafe_allow_html=True)
    st.markdown("#### <font color='#6e6e6e'>"
                "&nbsp;&nbsp;&nbsp;- **[SQL(Intermediate) from HackerRank](https://www.hackerrank.com/certificates/c9b2216b3c09)**<br></font>",
                unsafe_allow_html=True)


elif page == "Projects":
    Projects = option_menu("",
                       options=['Analysis & Visualization', 'Projects on BI Tools', 'Prediction Projects', 'LLM Based Projects'],
                       default_index=0,
                       orientation='horizontal')
    if Projects == "LLM Based Projects":
        st.markdown("<h3 style='color: #0a1828;'><b>Docx Translator:</b></h3>", unsafe_allow_html=True)
        st.markdown("""<p style='color: #0a1828;'>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- This feature will assist users in translating content in the docx format from one language to another. It also includes automatic name localization based on the user's selected region.
                    </P""", unsafe_allow_html=True)
        mention(label="Streamlit App", icon="streamlit",
                url="https://doctranslator-selvamaniind.streamlit.app/", )
        mention(label="Github Repo", icon="github", url="https://github.com/selvamani1992/DocTranslator", )

    elif Projects == "Prediction Projects":
        st.markdown("<h3 style='color: #0a1828;'><b><br>Broadband User Churn Prediction:</b></h3>", unsafe_allow_html=True)
        st.markdown("""<p style='color: #0a1828;'>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Churn prediction is a crucial task in customer relationship management as it helps businesses identify customers who are likely to leave or "churn" and take proactive measures to retain them.
                        </P""", unsafe_allow_html=True)
        mention(label="Streamlit App", icon="streamlit", url="https://churnprediction-broadband.streamlit.app/", )
        mention(label="Github Repo", icon="github", url="https://github.com/selvamani1992/Churn_Prediction")

        st.markdown("<h3 style='color: #0a1828;'><b><br>Diabetes Prediction:</b></h3>", unsafe_allow_html=True)
        st.markdown("""<p style='color: #0a1828;'>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- By utilizing this advanced machine learning model, we will be equipped with the capability to accurately forecast the probability of diabetes occurrence among expectant mothers.
                            </P""", unsafe_allow_html=True)
        mention(label="Streamlit App", icon="streamlit", url="https://diabetesprediction-selvamaniind.streamlit.app", )
        mention(label="Github Repo", icon="github", url="https://github.com/selvamani1992/DiabetesPrediction")

        st.markdown("<h3 style='color: #0a1828;'><b><br>Loan Approval Prediction:</b></h3>", unsafe_allow_html=True)
        st.markdown("""<p style='color: #0a1828;'>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- With the assistance of this machine learning model, we can assess an individual's eligibility for obtaining a loan. By analyzing multiple parameters, this model possesses the capability to deliver accurate predictions and promote fair lending practices.
                    </P""", unsafe_allow_html=True)
        #mention(label="Streamlit App", icon="streamlit", url="", )
        mention(label="Github Repo", icon="github", url="https://github.com/selvamani1992/Loan_Approval_Prediction" )

        st.markdown("<h3 style='color: #0a1828;'><b><br>Breast Cancer Prediction:</b></h3>", unsafe_allow_html=True)
        st.markdown("""<p style='color: #0a1828;'>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Developed a model that accurately predicts the likelihood of breast cancer in patients. Through analyzing the available data, performing data preprocessing, and utilizing advanced machine learning algorithms.
                        </P""", unsafe_allow_html=True)
        # mention(label="Streamlit App", icon="streamlit", url="", )
        mention(label="Github Repo", icon="github", url="https://github.com/selvamani1992/Breast_Cancer_Prediction")


    elif Projects == "Analysis & Visualization":
        st.markdown("<h3 style='color: #0a1828;'><b><br>Data Analysis on Delivery Charges:</b></h3>", unsafe_allow_html=True)
        st.markdown("""<p style='color: #0a1828;'>
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Analysis of the charges levied by their Delivery partners to X company per Order are correct or not and action plans to fix the difference.
                                </P""", unsafe_allow_html=True)
        # mention(label="Streamlit App", icon="streamlit", url="", )
        mention(label="Github Repo", icon="github", url="https://github.com/selvamani1992/DA_Analysis_on_charges")

        st.markdown("<h3 style='color: #0a1828;'><b><br>Youtube Data Harvesting and Warehousing:</b></h3>",
                    unsafe_allow_html=True)
        st.markdown("""<p style='color: #0a1828;'>
                                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- The process involves scraping comprehensive channel information from YouTube using the Google API. This data is then stored in MongoDB and later migrated to SQL for further analysis and management. Finally, the data is projected for FAQ purposes, allowing for easy access and utilization.
                                    </P""", unsafe_allow_html=True)
        # mention(label="Streamlit App", icon="streamlit", url="", )
        mention(label="Github Repo", icon="github", url="https://github.com/selvamani1992/YoutubeDataHarvesting.py")

        st.markdown("<h3 style='color: #0a1828;'><b><br>Phonepe Pulse Visualization:</b></h3>",
                    unsafe_allow_html=True)
        st.markdown("""<p style='color: #0a1828;'>
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Performing ETL and EDA on Phonepe data can provide valuable insights into the recent trends of online transactions. By analyzing various scenarios and visualizing the data through different plotting techniques, we can gain a deeper understanding of the patterns and dynamics at play.
                                        </P""", unsafe_allow_html=True)
        # mention(label="Streamlit App", icon="streamlit", url="", )
        mention(label="Github Repo", icon="github", url="https://github.com/selvamani1992/PhonepePulse")

        st.markdown("<h3 style='color: #0a1828;'><b><br>ISS Live Location Tracking:</b></h3>", unsafe_allow_html=True)
        st.markdown("""<p style='color: #0a1828;'>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Extract the live location information of the International Space Station and display it on a geoMap.
                            </P""", unsafe_allow_html=True)
        # mention(label="Streamlit App", icon="streamlit", url="", )
        mention(label="Github Repo", icon="github", url="https://github.com/selvamani1992/Iss_Live_Location")

    elif Projects == "Projects on BI Tools":

        st.markdown("<h3 style='color: #0a1828;'><b><br>Sales Data Analysis:</b></h3>", unsafe_allow_html=True)
        st.markdown("""<p style='color: #0a1828;'>
                                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- This project is to analyze sales data to identify trends, top-selling products, and revenue metrics for informed business decision-making.
                                            </P""", unsafe_allow_html=True)
        hr_att_analysis = """<iframe title="Sales Data" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNTUwNjUzYjItN2FiNC00ODIzLWJiYzktZGJlNGEwZWFjZTU1IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" frameborder="0" allowFullScreen="true"></iframe>"""
        st.components.v1.html(hr_att_analysis, height=400)

        st.markdown("<h3 style='color: #0a1828;'><b><br>HR Attrition Analysis:</b></h3>", unsafe_allow_html=True)
        st.markdown("""<p style='color: #0a1828;'>
                                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- A dashboard give 360° view of attrition/retention chances based on Demography, Job Nature and Wellness.
                                            </P""", unsafe_allow_html=True)
        hr_att_analysis = """<iframe title="HR Attrition Analytics" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNzFmYzFjOGQtOTRmYS00NzFiLWE0ZWYtY2EyNzAwZDFhNTE2IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9&embedImagePlaceholder=true" frameborder="0" allowFullScreen="true"></iframe>"""
        st.components.v1.html(hr_att_analysis, height=400)


elif page == 'Contact':
    st.markdown(
        "<p style='color: white;'><strong>Reach out to me via the form below or by emailing me at <a href='mailto:selvamani.ind@gmail.com' style='color: white;'>selvamani.ind@gmail.com</a>. You can also connect with me on <a href='https://www.linkedin.com/in/selvamani-a-795580266/' style='color: white;'>LinkedIn</a> or <a href='https://github.com/selvamani1992' style='color: white;'>GitHub</a>.</strong></p>",
        unsafe_allow_html=True)
    contact_form = """
    <form action="https://formsubmit.co/selvamani.ind@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <input type="hidden" name="_autoresponse" value="Auto-reply: Thank you for reaching out. We appreciate your message and it will be reviewed promptly. We will contact you back as soon as possible.">
         <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")
