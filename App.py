import streamlit as st
import random
import time

# पेज कॉन्फ़िगरेशन
st.set_page_config(page_title="For Navya ❤️", page_icon="🌹")

# --- सेशन स्टेट्स (डेटा स्टोर करने के लिए) ---
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'is_forgiven' not in st.session_state:
    st.session_state.is_forgiven = False

# 'No' बटन के बदलते हुए मैसेजेस
no_messages = [
    "No 😠", 
    "Sach mai? 🥺", 
    "Phir soch lo... 🤔", 
    "Phir ek bar phir se... 🧐", 
    "Sorry na bebe... Plzzz? 🎀", 
    "Otheeeeee... ❤️"
]

# --- CSS: बैकग्राउंड, बटन और हार्ट एनीमेशन ---
st.markdown("""
    <style>
    /* सुंदर पिंक ग्रेडिएंट बैकग्राउंड */
    .stApp {
        background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    }
    
    /* बटन स्टाइलिंग */
    .stButton>button {
        border-radius: 30px;
        border: 2px solid #ff4b4b;
        background-color: white;
        color: #ff4b4b;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff4b4b;
        color: white;
    }

    /* गिरने वाले दिलों का एनीमेशन */
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .heart {
        position: fixed;
        top: -10%;
        user-select: none;
        pointer-events: none;
        z-index: 9999;
        animation: fall 3s linear forwards;
    }

    /* "I Love You" टेक्स्ट एनीमेशन */
    .love-text {
        text-align: center;
        color: white;
        font-size: 45px;
        font-weight: bold;
        text-shadow: 3px 3px #ff4b4b;
        animation: heartbeats 1.5s infinite;
    }
    @keyframes heartbeats {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)

# दिलों की बारिश का फंक्शन
def rain_hearts(heart_type):
    heart_html = ""
    for _ in range(25):
        left = random.randint(0, 100)
        duration = random.uniform(2, 4)
        size = random.randint(20, 40)
        heart_html += f'<div class="heart" style="left:{left}%; animation-duration:{duration}s; font-size:{size}px;">{heart_type}</div>'
    st.markdown(heart_html, unsafe_allow_html=True)

# --- मुख्य लॉजिक (UI) ---

if not st.session_state.is_forgiven:
    st.markdown("<h1 style='text-align: center; color: white;'>Hi Navya... ❤️</h1>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h4 style='text-align: center; color: #4a4a4a;'>I know I messed up. Can we please fix this?</h4>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes, Maaf kiya! 😍"):
            st.session_state.is_forgiven = True
            st.rerun()

    with col2:
        if st.session_state.no_count < len(no_messages):
            current_no_text = no_messages[st.session_state.no_count]
            if st.button(current_no_text):
                # अगर 'Otheeeee' दबाया तो माफ़ कर दिया, वरना टूटे दिल गिरेंगे
                if "Otheeeeee" in current_no_text:
                    st.session_state.is_forgiven = True
                else:
                    rain_hearts("💔")
                    st.session_state.no_count += 1
                st.rerun()
        else:
            st.write("Ab toh maaf kar do please... 🥺")

else:
    # --- माफ़ी के बाद का सरप्राइज़ (The Celebration) ---
    rain_hearts("❤️")
    st.balloons()
    
    # I Wanna Be Yours म्यूजिक (GitHub पर navya_audio.mp3 अपलोड करें या इस लिंक का उपयोग करें)
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", format="audio/mp3", autoplay=True)
    
    st.markdown("<div class='love-text'>I LOVE U NAVYA SO MUCH ❤️</div>", unsafe_allow_html=True)
    
    # आपका एनिमेटेड वीडियो (सुनिश्चित करें कि navya_video.mp4 GitHub पर है)
    try:
        video_file = open('navya_video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    except FileNotFoundError:
        st.info("Aryan ❤️ Navya: Waiting for the sunset... ✨")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ4bmZ4bmZ4bmZ4/l4pTfx2qLs35wMSWk/giphy.gif", use_container_width=True)

    st.markdown("<h3 style='text-align: center; color: white;'>Everything is better with you! ✨</h3>", unsafe_allow_html=True)
