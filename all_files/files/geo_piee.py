import csv
import matplotlib.pyplot as plt


def analyze_csv(csv_file):
    country_counts = {}
    total_countries = 0

    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            country = row['country']
            if country not in country_counts:
                country_counts[country] = 0
            country_counts[country] += 1
            total_countries += 1

    # Find the most common countries
    most_common_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    # Print the result
    print("Top countries and their percentages:")
    for country, count in most_common_countries:
        percentage = (count / total_countries) * 100
        print(f"{country}: {percentage:.2f}%")

    # Pie chart
    labels = [country for country, _ in most_common_countries]
    sizes = [count for _, count in most_common_countries]

    plt.figure(figsize=(10, 6))
    plt.pie(sizes, labels=labels, startangle=140, labeldistance=1.1)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Top countries in the dataset')
    plt.show()


analyze_csv('merged_csv.csv')
