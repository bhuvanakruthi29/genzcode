import streamlit as st
from backend import get_ai_response
import time # Ensure this can handle a 'mode' parameter



# 1. Set page config (fix the path error here first!)
st.set_page_config(page_title="AI Code Cleaner", layout="wide")


# 1. Set page config (Must 


# 2. Check if the splash screen has already been shown
if 'initialized' not in st.session_state:
    placeholder = st.empty()
    with placeholder.container():
        # Center the logo and text
        st.markdown("<h1 style='text-align: center;'>Welcome to AI Code Cleaner</h1>", unsafe_allow_html=True)
        
        # Use your logo path
        st.image(r"C:\Users\soumy\Downloads\WhatsApp Image 2026-03-10 at 10.31.07 AM.jpeg", width=300) 
        
        st.markdown("<p style='text-align: center;'>Initializing system...</p>", unsafe_allow_html=True)
        time.sleep(2) # Keep splash screen for 2 seconds
    
    placeholder.empty() # Clear the splash screen
    st.session_state['initialized'] = True # Mark as done so it doesn't run again

# 4. Your actual application code starts here

# 4. Your actual application code starts here

# ... rest of your code ...
st.set_page_config(page_title="Code Refine AI", layout="wide")
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e1e2f 0%, #2d2d44 100%);
    }

    /* Force all text elements to White */
    .stApp, .stMarkdown,
    .stApp .stMarkdown,
    .stApp p,
    .stApp li,
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp h5,
    .stApp h6 {
    color: #ffffff !important;
    }

    /* Sidebar text color */
    [data-testid="stSidebar"] {
            background-color: #000
            }
    }
    /*sidebar navigation text*/
            [data-testid="stSidebar"] * {
            color:black!important;
            }
    .stButton >button{
             background: linear-gradient(45deg, #00dbde 0%, #fc00ff 100%);
    color:white;
    border:none;
            
    border-radius:10px;
    padding:0.5rem 2rem;
    font-weight:bold;
    trasition:0.3s;
 }               
    
    /* Input box text color (keeps text you type visible) */
    .stTextInput input {
        color:black !important; /* Keep input text dark so it's readable on white background */
    }
    </style>
    """, unsafe_allow_html=True)


# --- Sidebar Navigation ---
with st.sidebar:
    st.title("🚀 Navigation")
    page = st.radio("Go to:", ["Home","Code Optimization", "Settings"])
    
    st.divider()
    language = st.selectbox("Preferred Language", ["Python", "JavaScript", "C++", "Java"])

# --- Logic for Pages ---
if page == "Home":
    st.title('AI CODE-REFINE--"Think smarter code cleaner"')
    user_input = st.text_area("Ask a general question:")
    if st.button("Generate"):
        st.write(get_ai_response(user_input))


elif page=="Code Optimization":
    st.title("Code Optimization")
    st.write("content for code optimization goes here")

    
    # Tabs for different input methods
    tab1, tab2 = st.tabs(["📤 Upload File", "📝 Paste Code"])
       
    
    code_to_process = ""
    
    with tab1:
        uploaded_file = st.file_uploader("Choose a code file", type=['py', 'js', 'cpp', 'java'])
        if uploaded_file:
            code_to_process = uploaded_file.read().decode("utf-8")
            
    with tab2:
        code_to_process = st.text_area("Paste your code here:", height=300, placeholder="import math...")

    if st.button("Analyze & Optimize"):
        if code_to_process:
            col1, col2 = st.columns(2) # Side-by-side view for responsiveness
            
            with col1:
                st.subheader("Critique & Review")
                # Call backend with a 'review' flag
                review = get_ai_response(f"Review this code: {code_to_process}")
                st.info(review)
                
            with col2:
                st.subheader("Optimized Code")
                # Call backend with an 'optimize' flag
                optimized = get_ai_response(f"Optimize this code: {code_to_process}")
                st.code(optimized, language=language.lower())
        else:
            st.warning("Please provide some code first!")

elif page == "Settings":


    st.title("⚙️ Settings")
    st.text_area("Feedback")
    st.button("Submit Feedback")
