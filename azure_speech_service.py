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

def make_tts():
    print("INFO: FUNCTION REACHED")
    speech_config = speechsdk.SpeechConfig(subscription="X", region="germanywestcentral")
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

    print("INFO: CONFIG DONE")
    #result = synthesizer.speak_text_async("Hello").get()
    result = synthesizer.speak_text("Hello")

    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("file4.wav")

    print("INFO: STREAM GOING")
    if stream.status == stream.status.Canceled:
        return "an error happened, stream got canceled"
    if stream.status == stream.status.NoData:
        return "no data inside audio file" 
    if stream.status == stream.status.AllData:
        return "it was a success"

# make_tts()