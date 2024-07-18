#invoice making 
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
import os
from PIL import Image
import google.generativeai as genai


genai.configure(api_key=os.getenv("gemini_api"))

def get_gemini_response(input,image,prompt):
    #loading Model
    model=genai.GenerativeModel('gemini-pro-vision')
   
    response=model.generate_content([input,image[0],prompt])
    
    return response.text

def input_image_setup(upload_file):
    if upload_file is not None:
        bytes_data=upload_file.getvalue()
        image_parts=[{
            "mime_type":upload_file.type,
            "data":bytes_data

        }]
        return image_parts
    else:
        raise FileNotFoundError("no file detected")
    




 ############## StreamLit  APP    ##########   
st.set_page_config(page_title="Gemini Image invoice")
st.header("Gemini Application")
input=st.text_input("Input Prompt :",key="input")
uploaded_file=st.file_uploader("choose an imgae ...", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image=image,caption="uploaded image is ",use_column_width=True)
submit=st.button("tell me about the invoice")


input_prompt="""

You are an expert  in understanding invoices. You will recive input images as invoices
and you will have to answer the question based on the input image 




"""

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    print(response)

    st.write("the response is :",response)