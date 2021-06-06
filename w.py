import thinkdsp
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

plt.rcParams['font.sans-serif']=['SimHei']#图表上可以显示中文
plt.rcParams['axes.unicode_minus']=False#图表上可以显示负号


wave=thinkdsp.read_wave('328878__tzurkan__guitar-phrase-tzu.wav')
plt.subplot(3,3,1)
plt.title('原波形')
wave.plot()
wave.write(filename='out_put.wav')

segment=wave.segment(start=0.5,duration=1.5)
plt.subplot(3,3,2)
plt.title('截取0.5s后的音频')
segment.plot()

spectrum=wave.make_spectrum()
plt.subplot(3,3,3)
plt.title('频谱')
spectrum.plot()

spectrum.low_pass(cutoff=600,factor=0.001)
plt.subplot(3,3,7)
plt.title('经过低通滤波器后的频谱')
spectrum.plot()

spectrum.high_pass(cutoff=600,factor=0.001)
plt.subplot(3,3,8)
plt.title('经过高通滤波器后的频谱')
spectrum.plot()

spectrum.band_stop(low_cutoff=600,high_cutoff=1000)
plt.subplot(3,3,9)
plt.title('带阻滤波600-1000HZ的频谱')
spectrum.plot()
plt.show()
