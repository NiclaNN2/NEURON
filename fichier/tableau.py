from io import StringIO
import numpy as np
import scipy.io
from neuron import h

power=h.power
power=str(power)
fichiermatlab = 'chauffages_mat/test_sortie_'+power+'.mat'
doc_matlab = scipy.io.loadmat(fichiermatlab)
chauffage = doc_matlab["data"]
#print(chauffage)
nb_temps=chauffage.shape[0]
positions=chauffage.shape[1]

times_ms = chauffage[:,0]
