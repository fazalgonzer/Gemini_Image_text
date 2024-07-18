#invoice making 
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
import os
from PIL import Image
import google.generativeai as genai


genai.configure(api_key=os.getenv("gemini_api"))