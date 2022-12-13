import azure.cognitiveservices.speech as speechsdk


def make_tts():
    print("INFO: Function reached")
    speech_config = speechsdk.SpeechConfig(subscription="X", region="germanywestcentral")
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

    print("INFO: Config done")
    #result = synthesizer.speak_text_async("Hello").get()
    result = synthesizer.speak_text("Hello")

    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("file4.wav")

    print("INFO: Stream going")
    if stream.status == stream.status.Canceled:
        return "an error happened, stream got canceled"
    if stream.status == stream.status.NoData:
        return "no data inside audio file" 
    if stream.status == stream.status.AllData:
        return "it was a success"

# make_tts()