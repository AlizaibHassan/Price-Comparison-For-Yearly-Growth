import csv

def compare_prices(products):
    print("Product Comparison based on Growth Rate:")
    print("{:<15} {:<10} {:<15}".format("Product", "Price Diff", "Percentage Change"))

    result_rows = []

    for product in products:
        price_diff = product['Price'] - product['Old Price']
        percentage_change = (price_diff / product['Old Price']) * 100

        print("{:<15} {:<10.2f} {:<15.2f}%".format(
            product['Name'], price_diff, percentage_change))

        result_rows.append({
            'Product': product['Name'],
            'Price Diff': price_diff,
            'Percentage Change': percentage_change
        })

    # Save the comparison results to a new CSV file
    with open('price_comparison.csv', 'w', newline='') as result_file:
        fieldnames = ['Product', 'Price Diff', 'Percentage Change']
        writer = csv.DictWriter(result_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(result_rows)

if __name__ == "__main__":
    # Read data from the CSV file
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        products = list(reader)

    # Convert string values to float
    for product in products:
        for key in product:
            if key != 'Name':
                product[key] = float(product[key])

    # Compare prices based on growth rate and print/save the results
    compare_prices(products)
