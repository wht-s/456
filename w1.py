from wave import Wave_write
import thinkdsp
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号
wave=thinkdsp.read_wave('328878__tzurkan__guitar-phrase-tzu.wav')
cos_sig=thinkdsp.CosSignal(freq=440,amp=1.0,offset=0)
sin_sig=thinkdsp.SinSignal(freq=880,amp=0.5,offset=0)

mix=sin_sig+cos_sig
plt.subplot(1,2,1)
plt.title('叠加波形')
mix.plot()

wave=mix.make_wave(duration=0.5,start=0,framerate=11025)
spectrum=wave.make_spectrum()
plt.subplot(1,2,2)
plt.title('频谱')
spectrum.plot()

wave.write(filename='out_put2.wav')
plt.show()