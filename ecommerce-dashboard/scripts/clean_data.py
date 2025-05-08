import pandas as pd

try:
    #load data
    df = pd.read_csv("data/OnlineRetail.csv",encoding='ISO-8859-1')

    #log initial shape
    print("Initial Shape:",df.shape)

    #Handle missing values
    #remove rows with msiing customer id as it is essential for out analysis

    df = df.dropna(subset=["CustomerID"])
    print("Shape after removing missing CustomerID:", df.shape)

    #remove duplicates
    df = df.drop_duplicates()
    print("Shape after removing duplicates:",df.shape)

    #validate data
    #make sure sale was valid as price and quantity should be positive and non zero
    df = df[(df['Quantity']>0)&(df["UnitPrice"]>0)]
    print("Shape after removing invalid quantitie/prices:",df.shape)

    #standardize formats
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["CustomerID"] = df["CustomerID"].astype(int)
    df["Country"] = df["Country"].str.title()

    #add a total column
    df["TotalPrice"] = df["Quantity"]*df["UnitPrice"].round(2)

    #save cleaned data
    df.to_csv("data/OnlineRetailCleaned.csv",index=False)
    print("Cleaned dataset saved: data/OnlineRetailCleaned.csv")

except Exception as e:
    print(f"Error loading dataset: {e}")


