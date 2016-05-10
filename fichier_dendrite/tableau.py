from io import StringIO
import numpy as np
import scipy.io
from neuron import h

power=h.power
power=str(power)
fichiermatlab = 'chauffages_mat/quebec_500_'+power+'.mat'
doc_matlab = scipy.io.loadmat(fichiermatlab)
chauffage = doc_matlab["data"]
nb_temps=chauffage.shape[0]
positions=chauffage.shape[1]
