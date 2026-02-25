import pandas as pd

#Apply function to Series(columns)

df = pd.DataFrame({
    'name': ['sarah', 'mike', 'emma'],
    "age": [25,30, 28]
})

#Simple function
def clean_name(name):
    return name.strip().title()

df['name'] = df['name'].apply(clean_name())

#or with lambda
df['name'] = df['name'].apply(lambda x: x.strip().title())

#More complex function
def categorize_age(age):
    if age < 25:
        return 'Young'
    elif age < 35:
        return "adult"
    else:
        return "Senior"

df['age_group'] = df['age'].apply(categorize_age)

#Apply function to entire row
df = pd.DataFrame({
    'price': [100, 200, 150],
    'quantity': [5,3,8],
    'discount': [0.1, 0.15, 0.05]
})

#Access multiple columns in functions
def calculate_total(row):
    subtotal = row['price'] * row['quantity']
    discount_amount = subtotal * row['discount']
    return subtotal - discount_amount

df['total'] = df.apply(calculate_total, axis = 1)
#axis = 1 means apply to each row and axis = 0 means apply to each column

print(df)