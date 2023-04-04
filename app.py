import streamlit as st
import pandas as pd
from chatGPT_API import checkMessage
import pickle
import streamlit_ext as ste

checkMessage_obj = checkMessage()


st.markdown(
    """
    <style>
    .stButton>button {
        margin: 0 auto;
        display: block;
    }
    
    .output {
        background-color: #e0f0ff;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    
    .st-spinner {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    }
    
    </style>
    """,
    unsafe_allow_html=True,
)



st.title("ChatFact: Verify the Reliability of Your Messages with AI")
tab1, tab2 = st.tabs(["FactCheck", "Help"])
with tab1:
    st.markdown("""
    Please paste your message in the below text box """)
    uploaded_text = st.text_area('(max 3000 chars)', height=250, max_chars=3000)
    
    
    run = st.button("Check Message")

    if run:
        if len(uploaded_text) > 0 and uploaded_text.isspace()==False:
            input_text = str(uploaded_text)
            
            if len(input_text) > 3000:
                st.error("Length of you message exceeds 3000 characters. Please re-run with shorter message. Thanks!")
                st.stop()
            
            else:
                with st.spinner('Checking the message...'):
                    response_AI = checkMessage_obj.callChatGPT(input_text)
                    
                st.success('Done!')
                response_AI_points = response_AI.split('\n')
                response_AI_points = [x for x in response_AI_points if x.strip()]  # removing empty items
                st.subheader("Here's Fact Check Results:")
                #st.write(response_AI)
                #st.markdown(f'<div class="output">{response_AI}</div>', unsafe_allow_html=True)
                for point in response_AI_points:
                    st.markdown(f'<div class="output">{point}</div>', unsafe_allow_html=True)

        else:
            st.error("Please enter message")
            st.stop()


                    
                    


        
    
    
