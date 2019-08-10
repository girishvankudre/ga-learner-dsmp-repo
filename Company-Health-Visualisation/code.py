# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
#print (data.head())
loan_status = data['Loan_Status'].value_counts()
print (loan_status)
loan_status.plot(kind='bar')
plt.show()
#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
print (property_and_loan)
property_and_loan.plot(kind='bar',stacked=False,figsize=(15,10))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
print (education_and_loan)
education_and_loan.plot(kind='bar',stacked=True,figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
graduate = data[(data['Education']=='Graduate')]
not_graduate = data[(data['Education']=='Not Graduate')]
graduate['LoanAmount'].plot(kind='density',label='Graduate',figsize=(15,10))
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate',figsize=(15,10))
plt.legend()
plt.show()
#Code ends here

#For automatic legend display



# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3, ncols = 1, figsize=(15,10))
data.plot(kind='scatter',x='ApplicantIncome',y='LoanAmount',ax=ax_1)
plt.title('Applicant Income')
data.plot(kind='scatter',x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
plt.title('Coapplicant Income')
data['TotalIncome'] = data['ApplicantIncome'] + data ['CoapplicantIncome']
data.plot(kind='scatter',x='TotalIncome',y='LoanAmount',ax=ax_3)
plt.title('Total Income')
#print (data)


