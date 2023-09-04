import os
from sumerize import extract_keywords , ask_model
from record2text import speech_from_file, vision_from_file
from datetime import datetime
import streamlit as st
import openai


st.set_page_config(layout="wide")
st.title(":blue[Azure Cognitive Services]")
with st.sidebar:
    openai_key = st.text_input('OpenAI API Key', type='password', value=os.get_env('AZURE_OPENAI_KEY'))
    base = st.text_input('OpenAI API Base', value="https://openaione.openai.azure.com/" )
    model_name = st.text_input('Model Name', "text-davinci-003")
    st.divider()
    speech_key = st.text_input('Speech Key', type='password', value=os.get_env('AZURE_SPEECH_KEY'))
    lang = st.text_input('Speech Language',"en-US")
    st.divider()
    vision_key = st.text_input('Vision Key', type='password', value=os.get_env('AZURE_VISION_KEY'))
    vision_endpoint = st.text_input('Vision Endpoint', 'https://callcenter-vision.cognitiveservices.azure.com/')

    openai.api_type = "azure"
    openai.api_base = base 
    openai.api_version = "2022-12-01"
    openai.api_key = openai_key
        
st.image("https://k21academy.com/wp-content/uploads/2020/08/VisionSpeechLanguageDecisionWebSearch_Diagram-02.png")
st.divider()

date_string = datetime.now().strftime("%Y-%m-%d")
file_location_base = f'uploaded/{date_string}'
os.makedirs(os.path.dirname(file_location_base), exist_ok=True)

wav_uploaded_file = st.file_uploader("Audio:", type=["wav", "mp3"],accept_multiple_files=False)
if wav_uploaded_file:
    st.write(":blue[Converting to text and extracting keywords...]")
    wav_file_location = f'{file_location_base}/{wav_uploaded_file.name}'
    audio_bytes = wav_uploaded_file.read()
    with open(wav_file_location, "wb") as fs:
        fs.write(audio_bytes)
    if wav_file_location:
        text = speech_from_file(wav_file_location, speech_key, lang)
        st.audio(audio_bytes, format=wav_uploaded_file.type, start_time=0)
        st.write(text)
        st.write(extract_keywords(text,model_name))
        something = st.text_input('Ask from OpenAI completion API')
        words = text
        if something:
            st.write(ask_model(text, something, model_name))
st.divider()

jpg_uploaded_file = st.file_uploader("Image:", type=["jpg"],accept_multiple_files=False)
if jpg_uploaded_file:
    jpg_file_location = f'{file_location_base}/{wav_uploaded_file.name}'
    # jpg_file_location = f'uploaded/call-center-{datetime.now().strftime("%Y%m%d")}.jpg'
    if jpg_uploaded_file:
        st.write(":blue[Extracting image tags...]")
        image_bytes = jpg_uploaded_file.read()
        with open(jpg_file_location, "wb") as fs:
            fs.write(image_bytes)
        if jpg_file_location:
            st.image(jpg_file_location)
            st.write(vision_from_file(jpg_file_location, vision_key, vision_endpoint))

