import thinkdsp
from thinkdsp import Sinusoid
from thinkdsp import normalize,unbias
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np

#方波
class SquareSignal(Sinusoid):
    def evaliate(self,ts):
        cycles = self.freq*ts+self.offset/PI2
        frac,_ = np.modf(cycles)
        ys =self.amp*np.sign(unbias(frac))
        return ys

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


square = thinkdsp.SquareSignal(1100)
plt.subplot(2,1,1)
plt.ylabel('1100hz方波')
square.plot()

wave = square.make_wave(duration=0.5,framerate = 10000)
spectrum = wave.make_spectrum()
plt.subplot(2,1,2)
plt.ylabel('频谱')
spectrum.plot()



plt.show()