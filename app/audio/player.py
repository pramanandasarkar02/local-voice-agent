import simpleaudio as sa

def play_wav(path):
    wave = sa.WaveObject.from_wave_file(path)
    wave.play().wait_done()
