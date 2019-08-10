# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
#path = "Macintosh HD⁩/Users⁩/⁨pritigirishvankudre⁩/⁨Day3_Python/file.csv⁩⁩"
bank = pd.read_csv(path)
categorical_var=bank.select_dtypes(include='object')
print (categorical_var)
numerical_var=bank.select_dtypes(include='number')
print (numerical_var)

# code ends here


# --------------
# code starts here
banks = pd.DataFrame(bank.drop(['Loan_ID'],axis=1))
banks.isnull().sum()
bank_mode = banks.mode()
banks.fillna('bank_mode',inplace=True)
banks.isnull().sum()
#code ends here


# --------------
# Code starts here
import numpy as np
avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)


print (avg_loan_amount)

# code ends here



# --------------
# code starts here





loan_approved_se = banks[(banks['Self_Employed']=='Yes') &(banks['Loan_Status']=='Y')]['Self_Employed'].value_counts().sum()
print (loan_approved_se)
loan_approved_nse = banks[(banks['Self_Employed']=='No') &(banks['Loan_Status']=='Y')]['Self_Employed'].value_counts().sum()
print (loan_approved_nse)
banks['Loan_Status'].value_counts().sum()
percentage_se = ((loan_approved_se/banks['Loan_Status'].value_counts().sum())*100).round(2)
print (percentage_se)
percentage_nse = ((loan_approved_nse/banks['Loan_Status'].value_counts().sum())*100).round(2)
print (percentage_nse)
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: (x/12))

big_loan_term=len(loan_term[loan_term>=25])

print(big_loan_term)

# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')['Loan_Status','ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()



# code ends here


