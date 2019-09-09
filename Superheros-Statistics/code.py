# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#path of the data file- path
data = pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
#Code starts here 
gender_count = data['Gender'].value_counts()
print ("gender count")
print (gender_count)
plt.figure(figsize=(10,5))
plt.title('Gender Count')
gender_count.plot(kind='bar')
plt.show()


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print ('alignment')
print (alignment)
plt.title('Character Alignment')
alignment.plot(kind='pie')
plt.show()


# --------------
#Code starts here
import statistics as sts
sc_df = pd.DataFrame(data,columns=['Strength','Combat'])
sc_covariance = sc_df['Strength'].cov(sc_df['Combat'])
print ('covariance between Strength and Combat =',sc_covariance)
sc_strength = sts.stdev(sc_df['Strength'])
print ('Standard Deviation for Strength =',sc_strength)
sc_combat = sts.stdev(sc_df['Combat'])
print ('Standard Deviation for Combat =',sc_combat)
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print ("Pearson's correlational coefficient for Strength and Combat = ",sc_pearson)

ic_df = pd.DataFrame(data,columns=['Intelligence','Combat'])
ic_covariance = ic_df['Intelligence'].cov(ic_df['Combat'])
print ('covariance between Intelligence and Combat =',ic_covariance)
ic_intelligence = sts.stdev(ic_df['Intelligence'])
print ('Standard Deviation for Intelligence =',ic_intelligence)
ic_combat = sts.stdev(ic_df['Combat'])
print ('Standard Deviation for Combat =',ic_combat)
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print ("Pearson's correlational coefficient for Intelligence and Combat = ",ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)
print ('total_high =',total_high)
super_best = pd.DataFrame(data[(data['Total'] > total_high)])
print (super_best)
super_best_names = list(super_best['Name'])
print (super_best_names)


# --------------
#Code starts here
fig,axes = plt.subplots(nrows=1,ncols=3,figsize=(15,10))
ax_1 = axes[0]
ax_2 = axes[1]
ax_3 = axes[2]
ax_1.title.set_text('Intelligence')
ax_1.boxplot(data['Intelligence'])
ax_2.title.set_text('Speed')
ax_2.boxplot(data['Speed'])
ax_3.title.set_text('Power')
ax_3.boxplot(data['Power'])
plt.show()


