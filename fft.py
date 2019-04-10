<<<<<<< HEAD
# python3.7 前两个库需要另外安装,pylab在matplotlib中
import numpy
import pylab
import wave
import math
import cmath


class fft(object):
    data_right = []  # 右声道信号FFT后数据
    data_left = []  # 左声道信号FFT后数据
    wave_data = []  # 原始信号数据

    def __init__(self, filename):
        self.filename = filename
        self.nframes = 0
        self.framerate = 0
        self.get_data_from_file()

    # 对音频文件进行提取，只支持wav文件，并将数据存放在wava_data属性中
    def get_data_from_file(self):
        wave_file = wave.open(self.filename, "rb")
        self.nframes = wave_file.getnframes()
        self.framerate = wave_file.getframerate()
        wave_data_string = wave_file.readframes(self.nframes)
        self.wave_data = numpy.fromstring(wave_data_string, numpy.short)
        self.wave_data.shape = -1, 2
        self.wave_data = self.wave_data.T
        wave_file.close()

    # 对数据进行初始化，使用0将数据的长度填充至2的整数次方，
    # 并将数据的值按照蝶形运算的规律进行交换，方便以后的蝶形运算
    def data_init(self, data):
        lenght = len(data)
        m = math.ceil(math.log(lenght, 2))
        N = pow(2, m)
        data = numpy.append(data, numpy.zeros(N - lenght, dtype=numpy.complex))
        data = numpy.append(data, numpy.zeros(N, dtype=numpy.complex))
        data.shape = 2, -1
        for i in range(0, N, 1):
            if data[1][i] == 0:
                anti_i = int(bin(i)[2:].zfill(m)[::-1], 2)
                data[0][i], data[0][anti_i] = data[0][anti_i], data[0][i]
                data[1][i], data[1][anti_i] = 1, 1  # 表示这个两个值已经交换
        return data[0]

    def fft(self, data):
        data = self.data_init(data)
        N = len(data)
        M = math.log(N, 2)
        wn = cmath.exp(complex(0, -2 * numpy.pi / N))
        for m in range(1, int(M) + 1, 1):  # 按级进行运算
            b = 2 ** (m - 1)
            for r in range(0, b, 1):  # 按序蝶预算
                p = 2 ** (M - m) * r
                for k in range(r, N - 1, 2 ** m):  # 每序依次运算
                    temp = data[k] + data[k + b] * wn ** (p)
                    data[k + b] = data[k] - data[k + b] * wn ** (p)
                    data[k] = temp
        return data

    # 结果分析并绘图
    def show(self):
        self.data_left = self.fft(self.wave_data[0])  # 左声道
        self.data_right = self.fft(self.wave_data[1])  # 右声道

        # 原始信号，双声道
        time_axis = numpy.arange(0, self.nframes) * (1.0 / self.framerate)
        pylab.subplot(221)
        pylab.plot(time_axis, self.wave_data[0], linewidth=0.6)
        pylab.plot(time_axis, self.wave_data[1], c="r", linewidth=0.6)
        pylab.xlabel("time (seconds)")
        pylab.title('Original wave')

        # FFT后结果，双声道
        pylab.subplot(222)
        x_axis = numpy.arange(0, self.framerate, self.framerate / len(self.data_left))
        pylab.plot(x_axis, self.data_left, linewidth=0.8)
        pylab.plot(x_axis, self.data_right, c='r', linewidth=0.8)
        pylab.xlabel("hertz (Hz)")
        pylab.title('FFT of Mixed wave(two sides frequency range)')

        # 单个声道结果
        pylab.subplot(223)
        x_axis = numpy.arange(0, self.framerate / 2, self.framerate / len(self.data_left))
        pylab.plot(x_axis, self.data_left[range(int(len(x_axis)))], linewidth=0.8)
        pylab.xlabel("hertz (Hz)")
        pylab.title('FFT of Mixed wave')

        # 单个声道归一化
        pylab.subplot(224)
        self.data_left = self.data_left / len(self.data_left) * 2
        x_axis = numpy.arange(0, self.framerate / 2, self.framerate / len(self.data_left))
        pylab.plot(x_axis, self.data_left[range(int(len(x_axis)))], linewidth=0.8)
        pylab.xlabel("hertz (Hz)")
        pylab.title('FFT of Mixed wave(normalization)')

        pylab.show()


if __name__ == "__main__":
    fft(r"mate.wav").show()
=======
# python3.7 前两个库需要另外安装,pylab在matplotlib中
import numpy
import pylab
import wave
import math
import cmath


class fft(object):
    data_right = []  # 右声道信号FFT后数据
    data_left = []  # 左声道信号FFT后数据
    wave_data = []  # 原始信号数据

    def __init__(self, filename):
        self.filename = filename
        self.nframes = 0
        self.framerate = 0
        self.get_data_from_file()

    # 对音频文件进行提取，只支持wav文件，并将数据存放在wava_data属性中
    def get_data_from_file(self):
        wave_file = wave.open(self.filename, "rb")
        self.nframes = wave_file.getnframes()
        self.framerate = wave_file.getframerate()
        wave_data_string = wave_file.readframes(self.nframes)
        self.wave_data = numpy.fromstring(wave_data_string, numpy.short)
        self.wave_data.shape = -1, 2
        self.wave_data = self.wave_data.T
        wave_file.close()

    # 对数据进行初始化，使用0将数据的长度填充至2的整数次方，
    # 并将数据的值按照蝶形运算的规律进行交换，方便以后的蝶形运算
    def data_init(self, data):
        lenght = len(data)
        m = math.ceil(math.log(lenght, 2))
        N = pow(2, m)
        data = numpy.append(data, numpy.zeros(N - lenght, dtype=numpy.complex))
        data = numpy.append(data, numpy.zeros(N, dtype=numpy.complex))
        data.shape = 2, -1
        for i in range(0, N, 1):
            if data[1][i] == 0:
                anti_i = int(bin(i)[2:].zfill(m)[::-1], 2)
                data[0][i], data[0][anti_i] = data[0][anti_i], data[0][i]
                data[1][i], data[1][anti_i] = 1, 1  # 表示这个两个值已经交换
        return data[0]

    def fft(self, data):
        data = self.data_init(data)
        N = len(data)
        M = math.log(N, 2)
        wn = cmath.exp(complex(0, -2 * numpy.pi / N))
        for m in range(1, int(M) + 1, 1):  # 按级进行运算
            b = 2 ** (m - 1)
            for r in range(0, b, 1):  # 按序蝶预算
                p = 2 ** (M - m) * r
                for k in range(r, N - 1, 2 ** m):  # 每序依次运算
                    temp = data[k] + data[k + b] * wn ** (p)
                    data[k + b] = data[k] - data[k + b] * wn ** (p)
                    data[k] = temp
        return data

    # 结果分析并绘图
    def show(self):
        self.data_left = self.fft(self.wave_data[0])  # 左声道
        self.data_right = self.fft(self.wave_data[1])  # 右声道

        # 原始信号，双声道
        time_axis = numpy.arange(0, self.nframes) * (1.0 / self.framerate)
        pylab.subplot(221)
        pylab.plot(time_axis, self.wave_data[0], linewidth=0.6)
        pylab.plot(time_axis, self.wave_data[1], c="r", linewidth=0.6)
        pylab.xlabel("time (seconds)")
        pylab.title('Original wave')

        # FFT后结果，双声道
        pylab.subplot(222)
        x_axis = numpy.arange(0, self.framerate, self.framerate / len(self.data_left))
        pylab.plot(x_axis, self.data_left, linewidth=0.8)
        pylab.plot(x_axis, self.data_right, c='r', linewidth=0.8)
        pylab.xlabel("hertz (Hz)")
        pylab.title('FFT of Mixed wave(two sides frequency range)')

        # 单个声道结果
        pylab.subplot(223)
        x_axis = numpy.arange(0, self.framerate / 2, self.framerate / len(self.data_left))
        pylab.plot(x_axis, self.data_left[range(int(len(x_axis)))], linewidth=0.8)
        pylab.xlabel("hertz (Hz)")
        pylab.title('FFT of Mixed wave')

        # 单个声道归一化
        pylab.subplot(224)
        self.data_left = self.data_left / len(self.data_left) * 2
        x_axis = numpy.arange(0, self.framerate / 2, self.framerate / len(self.data_left))
        pylab.plot(x_axis, self.data_left[range(int(len(x_axis)))], linewidth=0.8)
        pylab.xlabel("hertz (Hz)")
        pylab.title('FFT of Mixed wave(normalization)')

        pylab.show()


if __name__ == "__main__":
    fft(r"mate.wav").show()
>>>>>>> d6179df1d186d0390976351dc12926fc6731b48f
