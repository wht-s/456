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

class SawtoothSignal(Sinusoid):
    
    def evaluate(self, ts):

        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys
def spect(spectrum):
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

#三角波验证
wave = TriangleSignal(440).make_wave(duration=0.5)
spectrum = wave.make_spectrum()
plt.subplot(3,1,1)
spectrum.plot(high=10000)
spect(spectrum)

plt.ylabel('三角波验证')


#方波验证
wave = SquareSignal(440).make_wave(duration=0.5)
spectrum = wave.make_spectrum()
plt.subplot(3,1,2)
spectrum.plot(high=10000)
spect(spectrum)
plt.ylabel('方波验证')

#锯齿波验证
wave = SawtoothSignal(440).make_wave(duration=0.5)
spectrum = wave.make_spectrum()
plt.subplot(3,1,3)
spectrum.plot(high=10000)
spect(spectrum)
plt.ylabel('方波验证')


plt.show()
