# import numpy as np
# import matplotlib.pyplot as plt

# # Simular dados espectrais
# wavelength = np.linspace(400, 4000, 3600)
# intensity = np.exp(-((wavelength - 1000)**2) / (2 * 300**2))

# # Plotar o espectro
# plt.figure(figsize=(8, 4))
# plt.plot(wavelength, intensity)
# plt.title('Espectro ATR-FTIR simulado')
# plt.xlabel('Número de onda (cm^-1)')
# plt.ylabel('Intensidade')
# plt.grid(True)
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import find_peaks, savgol_filter

# def load_spectrum(filename):
#     data = np.genfromtxt(filename, delimiter=',', names=True)  # `names=True` usa a primeira linha como nomes de coluna
#     wavelength = data['ppm']
#     intensity = data['Intensidade']
#     return wavelength, intensity

# def preprocess_intensity(intensity):
#     """ Aplica suavização e correção de linha de base se necessário. """
#     # Suavização usando o filtro Savitzky-Golay
#     smoothed_intensity = savgol_filter(intensity, 51, 3)  # Janela de 51, polinômio de ordem 3
#     return smoothed_intensity

# def detect_peaks(intensity, height=None, distance=100):
#     """ Detecta picos no espectro. """
#     peaks, _ = find_peaks(intensity, height=height, distance=distance)
#     return peaks

# def plot_spectrum(wavelength, intensity, peaks):
#     """ Plota o espectro com os picos identificados. """
#     plt.figure(figsize=(10, 5))
#     plt.plot(wavelength, intensity, label='Intensity', color='blue')
#     plt.plot(wavelength[peaks], intensity[peaks], 'x', color='red', label='Peaks')
#     plt.title('Espectro ATR-FTIR com Picos Identificados')
#     plt.xlabel('Número de Onda (cm^-1)')
#     plt.ylabel('Intensidade')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# # Uso do script
# filename = 'dados.csv'
# wavelength, intensity = load_spectrum(filename)
# smoothed_intensity = preprocess_intensity(intensity)
# peaks = detect_peaks(smoothed_intensity, height=0.1)  # Altura mínima do pico
# plot_spectrum(wavelength, smoothed_intensity, peaks)
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, savgol_filter

def load_spectrum(filename):
    """ Carrega os dados do espectro de um arquivo CSV. 
    Espera-se que a primeira linha contenha os nomes das colunas. """
    try:
        data = np.genfromtxt(filename, delimiter=',', names=True)
        wavelength = data['ppm']
        intensity = data['Intensidade']
        return wavelength, intensity
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None, None

def preprocess_intensity(intensity):
    """ Aplica suavização usando o filtro Savitzky-Golay. Ajusta o tamanho da janela baseado no tamanho do array. """
    window_length = len(intensity) if len(intensity) < 50 else 51  # Garante que a janela não seja maior que o array
    window_length = window_length if window_length % 2 == 1 else window_length - 1  # Janela deve ser ímpar
    try:
        smoothed_intensity = savgol_filter(intensity, window_length, 3)  # Ordem do polinômio 3
        return smoothed_intensity
    except Exception as e:
        print(f"Erro ao processar a intensidade: {e}")
        return intensity

def detect_peaks(intensity, height=None, distance=100):
    """ Identifica picos no espectro. """
    try:
        peaks, _ = find_peaks(intensity, height=height, distance=distance)
        return peaks
    except Exception as e:
        print(f"Erro ao detectar picos: {e}")
        return []

def plot_spectrum(wavelength, intensity, peaks):
    """ Plota o espectro com os picos identificados. """
    plt.figure(figsize=(10, 5))
    plt.plot(wavelength, intensity, label='Intensity', color='blue')
    plt.plot(wavelength[peaks], intensity[peaks], 'x', color='red', label='Peaks')
    plt.title('Espectro ATR-FTIR com Picos Identificados')
    plt.xlabel('Número de Onda (cm^-1)')
    plt.ylabel('Intensidade')
    plt.legend()
    plt.grid(True)
    plt.gca().invert_xaxis()  # Inverter o eixo x para conformidade com convenções espectrais
    plt.show()

# Uso do script
filename = 'dados.csv'
wavelength, intensity = load_spectrum(filename)
if wavelength is not None and intensity is not None:
    smoothed_intensity = preprocess_intensity(intensity)
    peaks = detect_peaks(smoothed_intensity, height=0.1)  # Altura mínima do pico
    plot_spectrum(wavelength, smoothed_intensity, peaks)
