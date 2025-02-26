import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Recommendation Web App", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
img1 = Image.open("images/course_image.jpg")
img2 = Image.open("images/download (4).jpeg")
img3 = Image.open("images/img(5).jpeg")
img4 = Image.open("images/img(4).jpeg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("GetRecommends")
    st.title("Unlock the potential of your data.")
    st.write(
        "Our goal is to create a recommendation system that accurately predicts users' preferences and recommends products that align with their interests, leading to increased customer satisfaction and improved conversion rates."
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What We do")
        st.write("##")
        st.write(
            """
            As a startup, success is often determined by your ability to use data to make informed decisions. Our recommendation system provides data-driven recommendations that help you to improve your customer experience, increase engagement, and drive conversions. With our system, you can take the guesswork out of marketing and focus on what really matters: building your business.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Our Categories")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img2)
    with text_column:
        st.subheader("Movie Recommendation")
        st.write(
            """
           Movie recommendation systems typically work by analyzing user data and movie features to generate personalized recommendations. We have used a content-based filtering approach to develop the movie recommendation system.

            """
        )
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img3)
    with text_column:
        st.subheader("Books Recommendation")
        st.write(
            """
            The recommendation system collects data from users, including their reading history, ratings, and interactions with books (e.g., purchases, reviews, bookmarks). This data is then used to build user profiles, which represent each user's preferences and interests. The system also gathers information about books, including their genres, authors, publication dates, and descriptions.

            """
        )

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img1)
    with text_column:
        st.subheader("Course Recommendation")
        st.write(
            """
          Courses recommendation system provides recommendation of selective and optional courses with respect to students' skills, knowledge, interests and free time slots in their timetables. We have used a content-based filtering approach to develop the courses recommendation system.

            """
        )



# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
