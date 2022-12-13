import os
import azure.cognitiveservices.speech as speechsdk

def make_stt():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription='X', region='germanywestcentral')
    speech_config.speech_recognition_language="en-US"

    
    # Recognize from file
    audio_config = speechsdk.audio.AudioConfig(filename="File4.wav")
    
    # Recognize from microphone
    # audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    # print("Speak into your microphone.")

    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return "Recognized: {}".format(speech_recognition_result.text)
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized: {}".format(speech_recognition_result.no_match_details)
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        return "Speech Recognition canceled: {} \n\n Error details: {}".format(cancellation_details.reason, cancellation_details.error_details)
        

# print(make_stt())

