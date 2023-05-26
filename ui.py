# 53-90
# install pyaudio
import pyaudio
  porcupine = None
pa = None
audio_stream = None

def setup_voice_control():
    try:
        global porcupine
        global pa
        global audio_stream
        porcupine = pvporcupine.create(keyword_paths=[
            'wake_word\\pause_game_windows_3_30_2021_v1.9.0\\pause_game_windows_2021-03-30-utc_v1_9_0.ppn',
            'wake_word\\play_game_windows_3_30_2021_v1.9.0\\play_game_windows_2021-03-30-utc_v1_9_0.ppn'],
            keywords=["blueberry", "grapefruit"])
            
        pa = pyaudio.PyAudio()
        print("loading complete")
        audio_stream = pa.open(
                            rate=porcupine.sample_rate,
                            channels=1,
                            format=pyaudio.paInt16,
                            input=True,
                            frames_per_buffer=porcupine.frame_length)
        return True
    except Exception as e:
        return False

def listen():
    global porcupine
    global pa
    global audio_stream
    pcm = audio_stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
    keyword_index = porcupine.process(pcm)
    print(keyword_index, end=' ')
    if keyword_index==0:
        return 'JUMP'
    elif keyword_index==1:
        return 'QUIT'