import requests
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_lottie import st_lottie

#title, emoji at www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":👤:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/Style.css")

#load assets
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_info = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_v9riyrep.json")
# Side bar
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu", #required
        options=["Home","Skills","Contact"], #required
    )
if selected == "Home":
    #header section
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Hi, I am Priyansh :wave:")
            st.title("A Computer Science Student From Gurgaon")
            st.write("Greetings! Welcome to my portfolio! I am thrilled to present my journey as a first-year student with a passion for programming and a strong foundation in Java, Python, C, MS Excel, and PowerPoint.")
            st.write("As a first-year student, I have just embarked on my academic and professional journey in the world of programming. Although I am in the early stages of my education, I am eager to showcase the projects I have undertaken and the skills I have acquired thus far.")
            st.write("My programming journey began with Java, Python, and C, where I have gained a solid understanding of the core concepts and principles. I have completed various coding assignments and projects that have honed my problem-solving skills and allowed me to implement practical solutions. Despite being in the early stages of my programming journey, I am committed to continuous learning and growth.")
            st.write("Furthermore, I have had the opportunity to work with MS Excel and PowerPoint, developing proficiency in these essential tools. Through coursework and personal projects, I have utilized Excel to analyze data, perform calculations, and create organized spreadsheets. Additionally, I have used PowerPoint to design visually appealing presentations to effectively convey information and ideas.")
            st.write("Although I am a first-year student, I am eager to take on new challenges and explore diverse programming opportunities. I am constantly seeking ways to expand my knowledge and skills, whether through online resources, coding communities, or collaborative projects with fellow students.")
            st.write("In my portfolio, you will find the projects I have completed, showcasing my programming abilities, problem-solving skills, and creative thinking. While I may not have an extensive professional background yet, I am excited to demonstrate my potential and commitment to learning.")
            st.write("Thank you for taking the time to review my portfolio. I am enthusiastic about the future and the possibilities it holds for me as a first-year student. I eagerly anticipate the chance to contribute my skills and collaborate on exciting projects in the near future.")
        with right_column:
            st_lottie(lottie_info, height=600, key="portfolio")

# what i have done
if selected == "Skills":
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Skills")
            st.write("##")
            st.write(
                """
                I have learned 3 Programming languages including\n
                - Python\n
                - Java\n
                - C \n
                I have a linkedin approved MS Excel skill\n
                I also have an introduction to PowerPoint Presentation
                """
            )
        with right_column:
            st_lottie(lottie_coding, height=300, key="developer")

#Contact
if selected =="Contact":
    with st.container():
        st.header("Get In Touch With Me!")
        st.write("##")
        #formsubmit.co/ Email Address
        contact_form = """
        <form action="https://formsubmit.co/dpriyansh23@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your Name" required>
             <input type="email" name="email" placeholder="Your Email" required>
             <textarea name="message" placeholder="Your Message" required></textarea>
             <button type="submit">Send</button>
        </form>
        """
        st.write("[LinkedIn](https://www.linkedin.com/in/priyansh-dahiya-b52428230/)")
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()