import streamlit as st


st.markdown(
    """
    <style>
    .stApp {
        background-color: #010b13; 
    }
    h1, h3 {
        text-align: center;
        color: #ffffff;  
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("🧠 Mad Libs Game")
st.subheader("Fill in the blanks to generate your hilarious daily routine!")


time_of_the_day1 = st.text_input("Enter a time of the day:")
verb_ending_in_ing1 = st.text_input("Enter a verb ending in -ing:")
body_part = st.text_input("Enter a body part:")
liquid = st.text_input("Enter a liquid:")
number = st.text_input("Enter a number:")
fruit = st.text_input("Enter a fruit:")
exercise = st.text_input("Enter an exercise:")
verb = st.text_input("Enter a verb:")
place = st.text_input("Enter a place:")
activity = st.text_input("Enter an activity:")
verb_ending_in_ing2 = st.text_input("Enter another verb ending in -ing:")
time_of_the_day2 = st.text_input("Enter another time of the day:")


if st.button("✨ Generate Story"):
    st.markdown("---")
    st.subheader("📖 Here's your crazy routine:")
    st.write(f"Every morning, I wake up at **{time_of_the_day1}** and start my life-changing routine.")
    st.write(f"First, I start **{verb_ending_in_ing1}** my **{body_part}** to get the blood flowing.")
    st.write(f"Then, I dunk my face in a bucket of **{liquid}** exactly **{number}** times—refreshing!")
    st.write(f"Next, I grab a **{fruit}** peel and rub it all over my face for that glow.")
    st.write(f"To stay fit, I do some **{exercise}** before I **{verb}** over to the **{place}** for a quick dip.")
    st.write(f"After that, I settle down to **{activity}** and clear my mind.")
    st.write(f"Finally, I spend some time **{verb_ending_in_ing2}** in my journal until **{time_of_the_day2}**, when I’m ready to conquer the world!")
