# Pandas: Changing the column type to Categorical

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 5, 3, 8],
    'salary': [189.1, 180.2, 190.3, 205.4],
})

df['name'] = df['name'].astype('category')

print(df)

print('-' * 50)

print(df.dtypes)
