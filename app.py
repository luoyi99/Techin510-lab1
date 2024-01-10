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
col1.markdown("I am a UX designer who graduated from the University of California, Irvine,\
            and previously working at VIVO as a UX designer on IoT and IoV-related products.\
            My design approach is one that values research, collaboration, testing, and iteration, while balancing business goals and user needs.  \
            I am open to new opportunities that can help expand my understanding of how design can help amplify human experiences.")

# education
col2.subheader("Education",divider = "grey")
col2.markdown("B.S. in Informatics & B.S. in Mathematics **@ University of California, Irvine**")
col2.markdown("M.S. in Technology Innovation **@ University of Washington**")

# work experience
col2.subheader("Work Experience",divider = "grey")
col2.markdown("UX Designer **@ VIVO**")

# hobbies and interests
col2.subheader("Hobbies and Interests",divider = "grey")
col2.markdown("stand-up comedy / travelling / food")


