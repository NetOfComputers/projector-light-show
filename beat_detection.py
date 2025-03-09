# audio_processor.py
import pyaudio
import numpy as np
import librosa
import time
import threading


class AudioProcessor:
    def __init__(self, callback, buffer_duration=5, SAMPLE_RATE=22050, CHUNK_SIZE=2048):
        self.callback = callback  # Callback to send BPM data to the LightShowApp class
        self.SAMPLE_RATE = SAMPLE_RATE
        self.CHUNK_SIZE = CHUNK_SIZE
        self.buffer_duration = buffer_duration  # Duration to accumulate audio before calculating BPM
        self.buffer = np.array([])  # Initialize an empty buffer to accumulate audio
        self.N_FFT = 2048
        self.HOP_LENGTH = 512
        self.stream = None
        self.running = True
        self.last_bpm = 0

    def start_audio_stream(self):
        p = pyaudio.PyAudio()
        self.stream = p.open(format=pyaudio.paInt16,
                             channels=1,
                             rate=self.SAMPLE_RATE,
                             input=True,
                             frames_per_buffer=self.CHUNK_SIZE)

        print("Starting audio stream. Press Ctrl+C to stop.")
        
        # Start the timer to update BPM every 5 seconds
        while self.running:
            audio_data = self.stream.read(self.CHUNK_SIZE)
            self.process_audio_data(audio_data)
            time.sleep(0.1)  # Small sleep to avoid busy-waiting

    def stop(self):
        self.running = False
        self.stream.stop_stream()
        self.stream.close()

    def process_audio_data(self, audio_data):
        # Convert the audio data to numpy array and normalize
        audio_data = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32)
        audio_data /= np.max(np.abs(audio_data))  # Normalize audio data

        # Append the audio data to the buffer
        self.buffer = np.concatenate((self.buffer, audio_data))

        # If the buffer is large enough (i.e., 5 seconds of audio), calculate the BPM
        if len(self.buffer) >= self.buffer_duration * self.SAMPLE_RATE:
            bpm = self.estimate_tempo(self.buffer)
            if bpm is not None and bpm != self.last_bpm:  # Avoid repeated BPM if it's the same
                self.callback(bpm)  # Call the callback method with the new BPM
                self.last_bpm = bpm
            # Reset buffer after calculating BPM
            self.buffer = np.array([])

    def estimate_tempo(self, audio_data):
        # Use librosa to calculate the onset envelope and tempo from the audio data
        onset_env = librosa.onset.onset_strength(y=audio_data, sr=self.SAMPLE_RATE, n_fft=self.N_FFT, hop_length=self.HOP_LENGTH)
        onset_env_mean = librosa.util.normalize(onset_env)  # Normalize onset envelope
        tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env_mean, sr=self.SAMPLE_RATE)
        return tempo[0] if tempo.size > 0 else None
