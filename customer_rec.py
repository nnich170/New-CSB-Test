import pandas as pd

record = pd.DataFrame({"Customers Name":["Sem Sovankanitha", "Horn Narak", "Yorn Rothana", "Deth Sokunboranich", "Bob Peterson", "ALice Wonderland", "Peter Kevinsky", "Marias Debbelo", "Jennie Kim", "Taylor Swift"], 
                       "Drinks":[100, 50, 80, 70, 33, 55, 20, 95, 32, 10]})

record["Status"] = ""  # Initialize an empty Status column
for index, drinks in enumerate(record["Drinks"]):
    if drinks > 50:
        record.loc[index, "Status"] = "G"
    elif drinks > 30:
        record.loc[index, "Status"] = "S"
    else:
        record.loc[index, "Status"] = "Non-Member"

record.to_csv(r"/Users/kanithasem/python test/.vscode/final_project/customers.csv", index=False)
record = pd.read_csv(r"/Users/kanithasem/python test/.vscode/final_project/customers.csv")

print(record)
