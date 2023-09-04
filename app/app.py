from audio_recorder_streamlit import audio_recorder
from sumerize import find_keywords , find_something
from record2text import speech_from_file, vision_from_file
from os.path import isfile, join
from datetime import datetime
import streamlit as st
from os import listdir
import openai
import os 


st.set_page_config(layout="wide")
st.title("Call Center")


# st.write("OPENAI RULEZ")
audio_bytes = audio_recorder(
    text="",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="user",
    icon_size="6x",
)

runner = True
with st.sidebar:
    custom =  st.checkbox('Configuration',True)
    if custom:
        openai_key = st.text_input('OpenAI API Key', type='password')
        base = st.text_input('OpenAI API Base', value="https://openaione.openai.azure.com/" )
        model_name = st.text_input('Model Name', "text-davinci-003")
        st.divider()
        speech_key = st.text_input('Speech Key', type='password')
        lang = st.text_input('Speech Language',"en-US")
        st.divider()
        vision_key = st.text_input('Vision Key', type='password')
        vision_endpoint = st.text_input('Vision Endpoint', 'https://callcenter-vision.cognitiveservices.azure.com/')

        openai.api_type = "azure"
        openai.api_base = base 
        openai.api_version = "2022-12-01"
        openai.api_key = openai_key
        
        runner =  st.checkbox('Submit')

        if runner:
            st.success('This is a success message!', icon="✅")
    else:
        try:
            model_name = "call-center"
            openai.api_type = "azure"
            openai.api_base = "https://openaione.openai.azure.com/" 
            openai.api_version = "2022-12-01"
            openai.api_key = os.getenv("KEY_AZURE_AI_DEVINCHI")
            speech_key = os.environ['KEY_AZURE_ML']
            vision_key = os.environ['VISION_KEY']
            vision_endpoint = os.environ['VISION_ENDPOINT']
            region_speech  =  "westeurope"
            lang = "en-US"
            runner = True
        except Exception as Error:
            runner = False
            pass
        
        st.success('This is a success message!', icon="✅")

# img = Image.open("images/top_spiderman.png")
# st.button(st.image(img))

if runner:
    selection = st.selectbox("How you want to start using call center :) ?", ["-- select ---", "from file", "from mic", "list existing"])

    if selection == "from mic":
        data_file = f'userdata/call-center-{datetime.now().strftime("%Y%m%d-%H%M%S")}.wav'
        audio_bytes = audio_recorder(pause_threshold=30)
        if audio_bytes:
           with open(data_file, "wb") as fs:
                fs.write(audio_bytes)

           st.audio(audio_bytes, format="audio/wav", start_time=0)  
           if st.button("Convert to Text"):
               st.write(speech_from_file(data_file,speech_key, lang))
           if  st.button("Extract Keywords"):
               st.write("finding keywords ...")
               st.write(speech_from_file(data_file,speech_key, lang))
               st.write(find_keywords(speech_from_file(data_file,lang,speech_key),model_name))

    elif selection == "from file":
        audio_bytes1 = st.file_uploader("Upload Files", type=["wav", "jpg"],accept_multiple_files=False)

        data_file_location = f'uploaded/call-center-{datetime.now().strftime("%Y%m%d")}.wav'

        if audio_bytes1:
            # st.write(type(audio_bytes1))
            audio_bytes2 = audio_bytes1.read()
            with open(data_file_location, "wb") as fs:
                fs.write(audio_bytes2)
            if data_file_location:
                st.audio(audio_bytes2, format="audio/wav", start_time=0)
                if st.button("Extract Image Tags"):
                   st.write(vision_from_file(data_file_location, vision_key, vision_endpoint))
                if st.button("Convert to Text"):
                   st.write(speech_from_file(data_file_location, speech_key, lang))
                if st.button("Convert to Text & Extract Keywords"):
                   st.write("finding keywords ...")
                   st.write(speech_from_file(data_file_location, speech_key, lang))
                   st.write(find_keywords(speech_from_file(data_file_location, speech_key,lang),model_name))
                if st.checkbox('Search Text (OpenAI Completion)'):
                   something = st.text_input('Enter what you would look to do')
                   words = speech_from_file(data_file_location, speech_key,lang)
                   if something:
                    st.write(find_something(words,something,model_name))

    elif selection == "list existing":
        selection = st.selectbox("Select file", ['uploaded','userdata'])
        if selection:
            selected = st.selectbox("Select file", [f for f in listdir(selection) if isfile(join(selection, f))])
            if selected:
                full_path = f'{selection}/{selected}'
                audio_file = open(full_path, 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/wav", start_time=0)
                if st.button("Convert to Text"):
                   st.write(speech_from_file(audio_file, speech_key, lang))
                if st.button("Extract Keywords"):
                   st.write("finding keywords ...")
                   st.write(speech_from_file(audio_file, speech_key, lang))
                   st.write(find_keywords(speech_from_file(audio_file, speech_key, lang),model_name))

