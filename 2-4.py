import thinkdsp
from thinkdsp import Sinusoid
from thinkdsp import normalize,unbias
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

#三角波
class TriangleSignal(Sinusoid):
    def evaluate(self,ts):
        cycles = self.freq*ts+ self.offset/PI2
        frac,_=np.modf(cycles)
        ys=np.abs(frac-0.5) 
        ys=normalize(unbias(ys),self.amp)
        return ys



signal1= thinkdsp.TriangleSignal(440).make_wave(duration = 0.01)

signal1.plot()

spectrum = signal1.make_spectrum()
print(spectrum.hs[0])
spectrum.hs[0]=100

spectrum.make_wave().plot(color='green')
plt.show()