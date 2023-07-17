import csv

def custom_sort(websites):
    # Separate numerical and alphabetical elements
    numerical_elements = []
    alphabetical_elements = []

    for website in websites:
        if website[0].isdigit():
            numerical_elements.append(website)
        else:
            alphabetical_elements.append(website)

    # Sort numerical elements
    numerical_elements.sort(key=lambda x: int(x.split('-')[0]))

    # Sort alphabetical elements
    alphabetical_elements.sort()

    # Combine sorted lists
    sorted_websites = numerical_elements + alphabetical_elements

    return sorted_websites

# Read websites from CSV file
def read_websites_from_csv(file_path):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        websites_list = [row[0] for row in reader]  # Assuming the website URLs are in the first column
    return websites_list

# Write sorted websites to a new CSV file
def write_sorted_websites_to_csv(file_path, sorted_websites):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for website in sorted_websites:
            writer.writerow([website])

# Example usage
input_csv_file = 'generic.csv'
output_csv_file = 'generic.csv'

websites_list = read_websites_from_csv(input_csv_file)
sorted_websites = custom_sort(websites_list)
write_sorted_websites_to_csv(output_csv_file, sorted_websites)

