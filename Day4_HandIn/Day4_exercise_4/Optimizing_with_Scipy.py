import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
#------------- Load data -----------------#
exp_data = np.load('I_q_IPA_exp.npy')
theo_data = np.load('I_q_IPA_model.npy')

#----------------- AI suggestion ----------------------#
mask = ~np.isnan(theo_data[:,0]) & ~np.isnan(theo_data[:,1])            # Remove NaNs from theoretical data.
theo_data_clean = theo_data[mask]
mask_exp = ~np.isnan(exp_data[:,0]) & ~np.isnan(exp_data[:,1])
exp_data_clean = exp_data[mask_exp]
theo_data_clean = theo_data_clean[np.argsort(theo_data_clean[:,0])]     # Sort by x (required for np.interp)
#-----------------------------------------------------#

#---------- Rescaling Theo data ------------------#
np.divide(theo_data_clean[:,1],10000,out=theo_data_clean[:,1])

theo_data_interp = np.interp(x=exp_data_clean[:,0],xp=theo_data_clean[:,0],fp=theo_data_clean[:,1])
theo_data_new = np.zeros((len(exp_data_clean[:,0]),2))
theo_data_new[:,0] = exp_data_clean[:,0]
theo_data_new[:,1] = theo_data_interp

scaling_param = 0
def func(scaling_param):
    diff = exp_data_clean[:,1] - scaling_param * theo_data_new[:,1]
    if np.isnan(diff).any():                                                        # AI suggestion
        return np.inf  # tell optimizer this is bad
    return np.sum(diff**2)
    
res = minimize_scalar(func, bounds=(0, 100), method='bounded')
print(res.fun)
print(res.x)
#------------------- Results -------------------#
#>>> 1576.4025466447881
#>>> 1.1551372039418375
#
scaled_theo = np.multiply(theo_data_new[:,1],res.x)     # Using scaling parameter to fit theoretical data.

#------------------- Plot the results ----------------------#
fig, ax1 = plt.subplots(figsize=(9.6,7.2))
fig.suptitle('Comparison of experimental and interpolated data before and after scaling')
InterpTheo, = ax1.plot(theo_data_new[:,0],theo_data_new[:,1],label='Interp Theo_data',color='b')
Scaled_Theo, = ax1.plot(theo_data_new[:,0],scaled_theo,label=f'Scaled Theo_data\nOptimal scaling param = {round(res.x,3)}',color='g')
Exp, = ax1.plot(exp_data_clean[:,0],exp_data_clean[:,1],label='Exp_data',color='darkorange')
ax1.set_xlabel('Scattering Vector')
ax1.set_ylabel('Scattering strength')
lines = [InterpTheo,Scaled_Theo, Exp]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper left')
plt.savefig('/...path_to_somewhere.../Day4_Optimizing_Scipy.png',dpi=300,format='png')
plt.tight_layout()
plt.show()

