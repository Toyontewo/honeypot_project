import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('cowrie_log.csv')

# Extract the "from_ip_address" column
ip_addresses = df['from_ip_address']

# Count occurrences of each IP address
ip_counts = ip_addresses.value_counts()

# Filter IP addresses with high occurrences (adjust threshold as needed)
high_occurrence_ips = ip_counts[ip_counts >= 10]

# Create a DataFrame with IP addresses and their counts
df_heatmap = pd.DataFrame({'IP Address': high_occurrence_ips.index, 'Count': high_occurrence_ips.values})

# Pivot the DataFrame for seaborn heatmap
heatmap_data = df_heatmap.pivot(index="IP Address", columns="Count", values="Count").fillna(0)

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, annot=True, fmt="g", cmap="YlGnBu")
plt.title('Heatmap of IP Addresses')
plt.xlabel('Count')
plt.ylabel('IP Address')
plt.show()
