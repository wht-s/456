import thinkdsp
from thinkdsp import Sinusoid
from thinkdsp import normalize,unbias
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np
#三角波
class TriangleSignal(Sinusoid):
    def evaluate(self,ts):
        cycles = self.freq*ts+ self.offset/PI2
        frac,_=np.modf(cycles)
        ys=np.abs(frac-0.5) 
        ys=normalize(unbias(ys),self.amp)
        return ys
    
#锯齿波    
class SawtoothSignal(Sinusoid):
    
    def evaluate(self, ts):

        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys

#方波
class SquareSignal(Sinusoid):
    def evaliate(self,ts):
        cycles = self.freq*ts+self.offset/PI2
        frac,_ = np.modf(cycles)
        ys =self.amp*np.sign(unbias(frac))
        return ys
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

signal1 = thinkdsp.SawtoothSignal(200)
plt.subplot(3,2,1)
plt.ylabel('200Hz锯齿波')
plt.title('波形')
signal1.plot()

sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=10000)
plt.subplot(3,2,2)
plt.title('频谱')
sawtooth.make_spectrum().plot()


signal2= thinkdsp.TriangleSignal(200)
plt.subplot(3,2,3)
plt.ylabel('200Hz三角波')
signal2.plot()

wave2 = signal2.make_wave(duration = 0.5,framerate = 10000)
spectrum = wave2.make_spectrum()
plt.subplot(3,2,4)

spectrum.plot()

signal3= thinkdsp.SquareSignal(200)
plt.subplot(3,2,5)
plt.ylabel('200Hz方波')
signal3.plot()

wave3 = signal3.make_wave(duration = 0.5,framerate = 10000)
spectrum = wave3.make_spectrum()
plt.subplot(3,2,6)

spectrum.plot()

plt.show()
