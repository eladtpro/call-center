import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from pydub import AudioSegment
import json
import io

import requests

#Convert the mp3 content into wav
def  convert_mp3_to_wav(mp3_data):
    audio = AudioSegment.from_mp3(io.BytesIO(mp3_data))
    audio = audio.set_frame_rate(16000)
    wav_data = io.BytesIO()
    audio.export(wav_data, format="wav")
    wav_data.seek(0)
    return  wav_data

# https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text?tabs=windows%2Cterminal&pivots=programming-language-python
def speech_from_file(data_file, speech_key,lang = "en-US", service_region="westeurope"):
    """performs one-shot speech recognition with input from an audio file"""
    # <SpeechRecognitionWithFile>
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = speechsdk.audio.AudioConfig(filename=data_file)
    # Creates a speech recognizer using a file as audio input, also specify the speech language
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, language=lang, audio_config=audio_config)

    # Starts speech recognition, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of 15
    # seconds of audio is processed. It returns the recognition text as result.
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query.
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    result = speech_recognizer.recognize_once()

    # Check the result
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return "**:blue[Recognized:]** {}".format(result.text)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized: {}".format(result.no_match_details)
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        res = "Speech Recognition canceled: {}".format(cancellation_details.reason)
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            res += "/n Error details: {}".format(cancellation_details.error_details)
        return res

    return 'result unknown'

def vision_from_file(data_file,vision_key,vision_endpoint, fixed = False):
    # # Images used for the examples: Describe an image, Categorize an image, Tag an image, 
    # # Detect faces, Detect adult or racy content, Detect the color scheme, 
    # # Detect domain-specific content, Detect image types, Detect objects
    
    if not fixed:
        # url = vision_endpoint + "vision/v3.1/analyze"
        url = vision_endpoint + "vision/v3.1/tag"
        headers = {'Ocp-Apim-Subscription-Key': vision_key,'Content-Type': 'application/octet-stream'}
        # params = {'visualFeatures': 'Categories,Description,Color'}
        with open(data_file, 'rb') as f:
            data = f.read()
        response = requests.post(
            url, headers=headers, data=data)
        response.raise_for_status()
        analysis = response.json()
        result = "**:blue[Tags:]**  \n"
        for tag in analysis['tags']:
            result += f"**{tag['name']}** with confidence {float(tag['confidence'])*100:.2f}%  \n"
            print(tag['name'], tag['confidence'])
        print(analysis)
        return result


    computervision_client = ComputerVisionClient(vision_endpoint, CognitiveServicesCredentials(vision_key))
    # remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
    remote_image_url = "https://whatconsumer.co.uk/wp-content/uploads/2008/07/broken_laptop_220-150x150.jpg"
    tags_result_remote = computervision_client.tag_image(remote_image_url )
    # Print results with confidence score
    print("Tags in the remote image: ")
    if (len(tags_result_remote.tags) == 0):
        return "No tags detected."
    else:
        # my_dict = {index: element for index, element in enumerate(tags_result_remote.tags)}
        # return json.dumps(my_dict, default=lambda o: o.__dict__, 
        #     sort_keys=True, indent=4)
        data = {}
        for tag in tags_result_remote.tags:
            data[tag.name] = tag.confidence
            # print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
        return json.dumps(data)

