import librosa
import pandas as pd


class FeatLibrosa:
    def __init__(self, sampling_rate, window_size_sec, window_stride_sec):
        self.sampling_rate = sampling_rate
        self.window_size_sec = window_size_sec
        self.window_stride_sec = window_stride_sec
        self.name = 'Librosa2'
        self.default_option = {'window': 'hann'}

    def feature_extraction(self, signal, **kwargs):
        window = kwargs.get('window', 'hann')

        df_feat = pd.DataFrame()
        n_fft = int(self.sampling_rate * self.window_size_sec)
        hop_length = int(self.sampling_rate * self.window_stride_sec)

        # feat
        feat0 = librosa.feature.spectral_rolloff(signal,
                                                  sr=self.sampling_rate,
                                                  n_fft=n_fft,
                                                  hop_length=hop_length,
                                                  window=window)

        df_feat['librosa_rolloff'] = feat0[0]
        return df_feat
