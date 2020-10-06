from rtlsdr import RtlSdr
import time, random, string, os
import numpy as np
import scipy.signal as signal


# def read_samples(sdr, freq):
#    F_offset = 250000  # shifted tune to avoid DC
#    sdr.center_freq = freq - F_offset
#    time.sleep(0.06)
#    iq_samples = sdr.read_samples(sample_rate * 0.25)  # sample 1/4 sec
#    fc1 = np.exp(-1.0j * 2.0 * np.pi * F_offset / sample_rate * np.arange(len(iq_samples)))  # shift down 250kHz
#    iq_samples = iq_samples * fc1
#    return iq_samples

def read_samples(sdr, freq):
    f_offset = 250000  # shifted tune to avoid DC
    sdr.center_freq = freq - f_offset
    time.sleep(0.06)
    iq_samples = sdr.read_samples(1221376)
    iq_samples = iq_samples[0:600000]
    fc1 = np.exp(-1.0j * 2.0 * np.pi * f_offset / sample_rate * np.arange(len(iq_samples)))  # shift down 250kHz
    iq_samples = iq_samples * fc1
    return iq_samples

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def collect_samples(freq, classname):
    os.makedirs("training_data/" + classname, exist_ok=True)
    os.makedirs("testing_data/" + classname, exist_ok=True)
    for i in range(0, 1000):
        iq_samples = read_samples(sdr, freq)
        iq_samples = signal.decimate(iq_samples, decimation_rate, zero_phase=True)
        if (i < 750):  # 75% train, 25% test
            filename = "training_data/" + classname + "/samples-" + randomword(16) + ".npy"
        else:
            filename = "testing_data/" + classname + "/samples-" + randomword(16) + ".npy"
        np.save(filename, iq_samples)
        if not (i % 10): print(i / 10, "%", classname)


sdr = RtlSdr()
sdr.sample_rate = sample_rate = 2400000
decimation_rate = 48
sdr.err_ppm = 56   # change it to yours
sdr.gain = 'auto'

# collect_samples(422600000, "tetra")
collect_samples(95000000, "wfm")
#collect_samples(104000000, "wfm")
collect_samples(942200000, "gsm")
#collect_samples(147337500, "dmr")
#collect_samples(49250000, "tv")

# collect "other" class training data
for freq in range(112000000, 130000000, 50000): #range(112000000, 174000000, 50000)
    print('Sampling at', freq)
    iq_samples = read_samples(sdr, freq)
    iq_samples = signal.decimate(iq_samples, decimation_rate, zero_phase=True)
    filename = "training_data/other/samples-" + randomword(16) + ".npy"
    np.save(filename, iq_samples)
    # 50/50 - train/test data
    iq_samples = read_samples(sdr, freq)
    iq_samples = signal.decimate(iq_samples, decimation_rate, zero_phase=True)
    filename = "testing_data/other/samples-" + randomword(16) + ".npy"
    np.save(filename, iq_samples)
