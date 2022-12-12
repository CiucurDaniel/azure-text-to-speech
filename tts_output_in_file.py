import azure.cognitiveservices.speech as speechsdk


speech_config = speechsdk.SpeechConfig(subscription="X", region="germanywestcentral")
speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

result = synthesizer.speak_text_async("Hello").get()
stream = speechsdk.AudioDataStream(result)
stream.save_to_wav_file("file.wav")

if stream.status == stream.status.Canceled:
    print("an error happened, stream got canceled")
if stream.status == stream.status.NoData:
    print("no data inside audio file") 
if stream.status == stream.status.AllData:
    print("it was a success")
