import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os

import requests

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
        return "Recognized: {}".format(result.text)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized: {}".format(result.no_match_details)
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        res = "Speech Recognition canceled: {}".format(cancellation_details.reason)
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            res += "/n Error details: {}".format(cancellation_details.error_details)
        return res

    return 'result unknown'

def vision_from_file(data_file,vision_key,vision_endpoint):
    # # Images used for the examples: Describe an image, Categorize an image, Tag an image, 
    # # Detect faces, Detect adult or racy content, Detect the color scheme, 
    # # Detect domain-specific content, Detect image types, Detect objects

    # computervision_client = ComputerVisionClient(vision_endpoint, CognitiveServicesCredentials(vision_key))
    # images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
    # remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
    # print("===== Tag an image - remote =====")
    # # Call API with remote image
    # tags_result_remote = computervision_client.tag_image(remote_image_url )

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

    print(analysis)


    return analysis



    # Print results with confidence score
    print("Tags in the remote image: ")
    if (len(tags_result_remote.tags) == 0):
        print("No tags detected.")
    else:
        for tag in tags_result_remote.tags:
            print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
    print()
    '''
    END - Tag an Image - remote
    '''
    print("End of Computer Vision quickstart.")

    # </SpeechRecognitionWithFile>


# def from_file(data_file,lang,endpoint_speech,speech_key):
#     speech_config = speechsdk.SpeechConfig(subscription=speech_key,
#                                            endpoint= endpoint_speech,
#                                            speech_recognition_language=lang
#                                            )
#     audio_input = speechsdk.AudioConfig(filename=data_file)
#     speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
#                                                    audio_config=audio_input,
#                                                    language=lang
#     )

#     # result = speech_recognizer.recognize_once_async().get()
#     result = speech_recognizer.recognize_once()
    
#     # Checks result.
#     if result.reason == speechsdk.ResultReason.RecognizedSpeech:
#         print("Recognized: {}".format(result.text))
#     elif result.reason == speechsdk.ResultReason.NoMatch:
#         print("No speech could be recognized: {}".format(result.no_match_details))
#     elif result.reason == speechsdk.ResultReason.Canceled:
#         cancellation_details = result.cancellation_details
#         print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#         if cancellation_details.reason == speechsdk.CancellationReason.Error:
#             print("Error details: {}".format(cancellation_details.error_details))
    
#     return(result.text)
