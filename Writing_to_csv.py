import pandas as pd

df = pd.DataFrame({
    'name': ['sarah', 'mike', 'emma'],
    "age": [25,30, 28],
    'city': ['Mumbai', 'Goa', "Mumbai"]
})

#Write to CSV
df.to_csv("raw_orders.csv", index= False)

#Appending to CSV
#First write
df.to_csv("raw_orders.csv", index= False)

#Append more data later
new_data = pd.DataFrame({'name': ['akanksha'], 'age':[30], 'city': ['Pune']})
new_data.to_csv("raw_orders.csv", index= False)
print(df)
