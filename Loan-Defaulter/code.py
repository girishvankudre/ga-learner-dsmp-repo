# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
#print (df.head())
print ("shape of data is ",df.shape)
fico = len(df[df['fico']>700].index)
print ("Fico score greater than 700 is ",fico)
p_a = (fico/df.shape[0])
print ("probablity that fico credit score is greater than 700 is ",p_a)

purpose = len(df[df['purpose']=='debt_consolidation'].index)
print ("purpose is debt_consolidation the qunatity is ",purpose)
p_b = (purpose/df.shape[0])
print ("probablity that purpose is debt_consolidation is ",p_b)

F_P = len(df[(df['purpose']=='debt_consolidation') & (df['fico']>700)].index)
print ("purpose is debt_consolidation and fico greater than 700, the qunatity is ",F_P)
p_F_P = (F_P/df.shape[0])
print ("probablity that purpose is debt_consolidation and fico greater than 700 is ",p_F_P)

df1 = [df['purpose']=='debt_consolidation']

p_a_b = p_F_P/p_a
print ("probablity that event purpose == 'debt_consolidation' given 'fico' credit score is greater than 700 is ",p_a_b)

result = p_a_b == p_b
print ("Variables are independent =",result)
# code ends here


# --------------
# code starts here
pbl = len(df[df['paid.back.loan']=='Yes'].index)
print ("paid back loan as Yes and qunatity is ",pbl)
prob_lp = (pbl/df.shape[0])
print ("probablity that loan paid back successfully is ",prob_lp)

cp = len(df[df['credit.policy']=='Yes'].index)
print ("credit policy as Yes and qunatity is ",cp)
prob_cs = (cp/df.shape[0])
print ("probablity that credit policy followed is ",prob_cs)

new_df = df[df['paid.back.loan']=='Yes']

pbl_cp = len(df[(df['credit.policy']=='Yes') & (df['paid.back.loan']=='Yes')].index)
print ("paid back loan as Yes and credit policy as Yes qunatity is ",pbl_cp)
prob_pbl_cp = (pbl_cp/df.shape[0])
print ("probablity that paid back loan as Yes and credit policy as Yes is ",prob_pbl_cp)

prob_pd_cs = prob_pbl_cp/prob_lp
print ("probablity that paid back loan as Yes given credit policy as Yes is ",prob_pd_cs)

bayes = (prob_pd_cs * prob_lp)/ prob_cs
print ("Value of bayes =",bayes)

# code ends here


# --------------
# code starts here
values = df['purpose'].value_counts()
#print (values)
#print (type(values))
#print (list(values))
plt.figure(figsize=(10,5))
plt.title("Visualize the bar plot for the feature purpose")
plt.bar(df['purpose'].unique(),height=list(values))
plt.xlabel('values for purpose column')
plt.ylabel('count for values')
plt.xticks(rotation=90)
plt.show()

df1 = df[df['paid.back.loan']== 'No']

values1 = df1['purpose'].value_counts()
plt.figure(figsize=(10,5))
plt.title("Visualize the bar plot for the feature purpose where paid.back.loan == No")
plt.bar(df1['purpose'].unique(),height=list(values1))
plt.xlabel('values for purpose column')
plt.ylabel('count for values')
plt.xticks(rotation=90)
plt.show()

# code ends here


# --------------
# code starts here
inst_median = np.median(df['installment'])
print ("median for installment =",inst_median)

inst_mean = np.mean(df['installment'])
print ("mean for installment =",inst_mean)

plt.figure(figsize=(10,5))
plt.title("Histogram for installment")
plt.hist(df['installment'])
plt.show()
plt.figure(figsize=(10,5))
plt.title("Histogram for log annual income")
plt.hist(df['log.annual.inc'])
plt.show()
# code ends here


