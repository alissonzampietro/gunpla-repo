import pandas as pd

model_kits = pd.read_csv('data/ModelKits.csv')
gundam_grades = pd.read_csv('data/GundamGrades.csv')
grades_to_kits = pd.read_csv('data/_GundamGradesToModelKits.csv')

# Merge the dataframes
# First merge grades with the mapping table
df = grades_to_kits.merge(
    gundam_grades,
    left_on='A',
    right_on='id',
    how='left'
)

# Then merge with the model kits
final_df = df.merge(
    model_kits,
    left_on='B',
    right_on='id',
    how='left'
)

# Clean up the columns (remove redundant IDs)
final_df = final_df.drop(['A', 'B', 'id_x', 'id_y'], axis=1)

# Display the first few rows
print(final_df.head())

# Save to a new CSV if needed
final_df.to_csv('data/combined_gunpla_data.csv', index=False)