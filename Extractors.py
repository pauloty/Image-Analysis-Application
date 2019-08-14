# Imports necessarios para execucao
import cv2
import csv
import glob
import numpy as np
from skimage import feature
from skimage import data
import matplotlib.pyplot as plt
import mahotas.features
import os
from scipy.stats import kurtosis, skew

# Executa o LBP sobre as imagens
def lbp(images, lbp_sampling_points, lbp_sampling_radius, method):

    # Limpa o plot
    plt.clf()
    images = []
    histograms = []

    # Como estava esperando o codigo da segmentacao ser modificado para python3, no momento eu recupero as imagens de um diretorio contendo
    # as imagens de alta e baixa densidade ja segmentadas
    files = glob.glob("D:\\User\\Desktop\\Histopathological-Image-Analysis-Application-master\\test" + '/*.png')
    for myFiles in files:
        img = cv2.imread(myFiles, cv2.IMREAD_GRAYSCALE)
        images.append(img)

    for img in images:
        features = feature.local_binary_pattern(img, lbp_sampling_points, lbp_sampling_radius, method=method)
        histograms.append(features)

    '''Alternativa salvando imagem
    plt.ylabel("% of Pixels")
    plt.xlabel("LBP pixel bucket")
    n_bins0 = int(histograms[0].max() + 1)
    n_bins1 = int(histograms[1].max() + 1)
    Barras lado a lado
    plt.hist([histograms[0].ravel(), histograms[1].ravel()], density=True, bins=n_bins0, range=(0, n_bins0), label=['high','low'])
    Barras sobrepostas
    plt.hist(histograms[0].ravel(), density=True, bins=n_bins0, range=(0, n_bins0), label='high')
    plt.hist(histograms[1].ravel(), density=True, bins=n_bins1, range=(0, n_bins1), alpha=0.5, label='low')
    plt.legend(loc='upper right')
    Salva o histograma em uma figura
    return plt.savefig('LBP_Result.png')'''

    return histograms

