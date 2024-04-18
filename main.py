import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import linregress

class DataAnalysis:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)
        self.x_log = None
        self.y_log = None
        self.x = None
        self.y = None
    
    def transform_data(self, x, y):
        self.x = self.df[x]
        self.y = self.df[y]
        self.x_log = np.log(self.x)
        self.y_log = np.log(self.y)

    def plot_data(self):
        plt.plot(self.x, self.y, marker='o', linestyle='', color='blue', label='Dados log-log')
        plt.grid(True)
        plt.title('Dados Originais')
        plt.xlabel('(x)')
        plt.ylabel('(y)')
        plt.savefig('Dados Originais')
        plt.show()
 
    def plot_data_log(self):
        plt.plot(self.x_log, self.y_log, marker='o', linestyle='', color='blue', label='Dados log-log')
        plt.grid(True)
        plt.title('Dados Originais em Log-Log')
        plt.xlabel('ln(x)')
        plt.ylabel('ln(y)')
        plt.savefig('Dados Originais em Log-Log')
        plt.show()
    
    def linear_regression(self):
        slope, intercept, r_value, _, _ = linregress(self.x_log, self.y_log)
        y_pred = intercept + slope * self.x_log
        plt.scatter(self.x_log, self.y_log, color='blue', marker='o', label='Dados log-log')
        plt.plot(self.x_log, y_pred, 'r', label=f'Linha de ajuste: inclinação={slope:.2f}, intercepto={intercept:.2f}')
        plt.xlabel('ln(x)')
        plt.ylabel('ln(y)')
        plt.title('Regressão Linear Log-Log com Erros Residuais')
        plt.legend()
        plt.grid(True)
        for xi, yi, yi_pred in zip(self.x_log, self.y_log, y_pred):
            plt.vlines(xi, yi_pred, yi, color='green')
        plt.savefig('Regressão Linear Log-Log com Erros Residuais')
        plt.show()
        print(f"Inclinação (m): {slope}")
        print(f"Intercepto: {intercept}")
        print(f"Coeficiente de determinação (R^2): {r_value**2}")
    
    def linear_regression_no_intercept(self):
        x_log_array = self.x_log.to_numpy()[:, np.newaxis]
        slope = np.linalg.lstsq(x_log_array, self.y_log, rcond=None)[0][0]
        y_pred = slope * self.x_log
        plt.scatter(self.x_log, self.y_log, color='blue', marker='o', label='Dados log-log')
        plt.plot(self.x_log, y_pred, 'r', label=f'Linha de ajuste: inclinação={slope:.2f}, intercepto=0')
        for xi, yi, yi_pred in zip(self.x_log, self.y_log, y_pred):
            plt.plot([xi, xi], [yi, yi_pred], 'g-')
        plt.xlabel('ln(x)')
        plt.ylabel('ln(y)')
        plt.title('Regressão Linear Log-Log sem Intercepto e Erros Residuais')
        plt.legend()
        plt.grid(True)
        plt.savefig('Regressão Linear Log-Log sem Intercepto e Erros Residuais')
        plt.show()
        r_value = np.corrcoef(self.x_log, self.y_log)[0, 1]
        r_squared = r_value**2
        print("Inclinação (m):", slope)
        print("Intercepto: 0 (forçado)")
        print("Coeficiente de determinação (R^2):", r_squared)

# Uso da classe
analysis = DataAnalysis('julgamentos.csv')
analysis.transform_data('Frequencia(Hz)', 'Julgamento_som')
analysis.plot_data()
analysis.plot_data_log()
analysis.linear_regression()
analysis.linear_regression_no_intercept()
