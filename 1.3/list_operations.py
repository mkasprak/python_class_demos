# list of delinquent account numbers
delinquent_accounts = [1056, 2008, 3278, 4189]

if 2008 in delinquent_accounts:
    print("The account number 2008 is delinquent.")
else:
    print("The account number 2008 is not delinquent.")

# check to see index of 2008
for i in range(len(delinquent_accounts)):
    if delinquent_accounts[i] == 2008:
        print("The account number 2008 is at index", i)  # 1
