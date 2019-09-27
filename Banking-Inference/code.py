# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings
import statistics

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]

#Code starts here
data = pd.read_csv(path)
data_sample = data.sample(n=sample_size,random_state=0)
sample_mean = statistics.mean(data_sample['installment'])
print ("sample mean installment =",sample_mean)
sample_std = statistics.stdev(data_sample['installment'])
print ("sample std installment =",sample_std)
margin_of_error = z_critical * (sample_std/math.sqrt(sample_size))
print ("margin_of_error =",margin_of_error)
confidence_interval = (sample_mean-margin_of_error,sample_mean+margin_of_error)
print ("confidence_interval =",confidence_interval)
true_mean = np.mean(data['installment'])
print ("true_mean =",true_mean)


# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(nrows=3,ncols=1)
plt.figure (figsize=(35,20))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=5.5, hspace=15.5)
fig.tight_layout()
for i in range(len(sample_size)):
    m = []
    for j in range(1000):
        data_installment = data['installment'].sample(n=sample_size[i],random_state=0)
        m.append(data_installment.mean())
    mean_series = pd.Series(m)
    axes[i].hist(mean_series)


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['int.rate'] = data['int.rate'].apply(lambda x : x.strip('%'))
#data['int.rate'] = (data['int.rate'].str[:-1].astype(float))
data['int.rate'] = (data['int.rate'].astype(float))/100
#print (data.head())
z_statistic, p_value = ztest(data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative='larger')
print("Z-statistics = ",z_statistic)
print("p-value = ",p_value)


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic, p_value = ztest(data[data['paid.back.loan']=='No']['installment'],data[data['paid.back.loan']=='Yes']['installment'])
print("Z-statistics = ",z_statistic)
print("p-value = ",p_value)


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[(data['paid.back.loan'] == 'Yes')]['purpose'].value_counts()
#print ("Count of purpose with paid back loan as Yes")
#print (type(yes))
#print (yes)
no = data[(data['paid.back.loan'] == 'No')]['purpose'].value_counts()
#print ("Count of purpose with paid back loan as No")
#print (type(no))
#print (no)
observed = pd.concat([yes,no], axis=1, keys=['Yes','No'])
print ("Concatenation of Yes and No Responses for Purpose column")
print (observed)
chi2, p, dof, ex = chi2_contingency(observed)
print ("chi2 =",chi2)
print ("p =",p)
print ("dof =",dof)
print ("ex =",ex)
print ("critical_value =",critical_value)


