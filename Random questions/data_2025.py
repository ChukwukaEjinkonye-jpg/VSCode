import pandas as pd
import matplotlib.pyplot as plt


data =  pd.read_csv('data_2025apr14.csv')

#print(round(data['repair_cost'].mean() , 2))
#print(data.describe())

#avg_repair_costs = data.groupby('defect_type')['repair_cost'].mean()
#avg_repair_costs = data.groupby('severity')['repair_cost'].mean()
avg_repair_costs = data.groupby('defect_date')

# plt.figure(figsize=(10, 6))
# avg_repair_costs.plot(kind='bar', color='skyblue')
# plt.title('Average Repair Cost by Defect Type')
# plt.xlabel('Defect Type')
# plt.ylabel('Average Repair Cost ($)')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()

print(data.groupby('defect_date').max())