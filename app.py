import streamlit as st

# title
st.title("YI'S PERSONAL WEBSITE")



# load the video file
video_file = open('src/memoji.MOV','rb')
video_bytes = video_file.read()

st.video(video_bytes)

# column layout
col1, col2 = st.columns(2)

# about
col1.subheader("About",divider = "grey")
col1.text("I am a UX designer who graduated from the\nUniversity of California, Irvine,\
            and currently working\n at VIVO as a UX designer on IoT and IoV-related products.\n\
            My design approach is one that values research, collaboration, testing, and iteration,\n while balancing business goals and user needs.  \
            I am open to new opportunities that can help expand my understanding of how design can help amplify human experiences.")

# education
col2.subheader("Education",divider = "grey")
col2.text("B.S. in Informatics & B.S. in Mathematics")
col2.text("@ University of California, Irvine")

# work experience
col2.subheader("Work Experience",divider = "grey")
col2.text("UX Designer @ VIVO")

# work experience
col2.subheader("Work Experience",divider = "grey")
col2.text("vivo - UX designer")

# hobbies and interests
col2.subheader("Hobbies and Interests",divider = "grey")
col2.text("stand-up comedy / travelling / food")


