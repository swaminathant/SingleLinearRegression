from ml import linearregression

ln = linearregression.SinglelinearRegression()

age = [18,25,57,45,26,64,37,40,24,33]
salary = [15000,29000,68000,52000,32000,80000,41000,45000,26000,33000]

ypredict = ln.Linear(age,salary)
print(ln.B1, ln.B0)
print(ypredict)
print("Predict age 22 salary is :",ln.Predict(22))
print("RMSE Value is :",ln.RMSE(ypredict, salary))
print("Pearsonr value is : ",ln.pearsonr(age,salary))