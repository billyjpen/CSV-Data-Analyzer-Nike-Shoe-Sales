import pandas as pd

def main():
    # Load the sales data from a CSV file
    file_path = 'sales.csv'
    df = pd.read_csv(file_path)

    # Display the entire DataFrame to provide an overview of the data
    print(df)

    # Prompt the user to select a category and gender for data filtering
    category_type = get_category()
    gender_type = get_gender()

    # Filter the data based on the selected category and gender
    data_filtered = df[(df['category'] == category_type) & (df['gender'] == gender_type)]

    # Prompt the user to choose the sorting order for quantity_sold
    assert_type = assert_quantity_sold()

    # Sort the filtered data based on the chosen sorting order
    if assert_type == "least to greatest":
        sort = data_filtered.sort_values(by='quantity_sold', ascending=True)
    elif assert_type == "greatest to least":
        sort = data_filtered.sort_values(by='quantity_sold', ascending=False)
    else:
        print(f'Invalid sorting option: "{assert_type}"')
        return

    # Display the filtered and sorted sales data
    print("\n*Sales data filtered*\n\n", sort)

def get_category():
    # Prompt the user to choose a category from the given options
    option = "Running, Basketball, Training, Casual, Vintage, Skateboarding"
    while True:
        try:
            category_type = input(f"\n{option}\nCategory: ").title().strip()
            if category_type in ['Running', 'Basketball', 'Training', 'Casual', 'Vintage', 'Skateboarding']:
                return category_type
            else:
                print(f'Invalid category: "{category_type}"')
        except Exception as e:
            print(f'Error: {e}')

def get_gender():
    # Prompt the user to choose a gender from the given options
    option = "Men, Women, Unisex"
    while True:
        try:
            gender_type = input(f"\n{option}\nGender: ").title().strip()
            if gender_type in ['Men', 'Women', 'Unisex']:
                return gender_type
            else:
                print(f'Invalid gender: "{gender_type}"')
        except Exception as e:
            print(f'Error: {e}')

def assert_quantity_sold():
    # Prompt the user to choose the sorting order for quantity_sold
    option = "least to greatest, greatest to least"
    while True:
        try:
            assert_type = input(f"\n{option}\nSort: ").lower()
            if assert_type in ['least to greatest', 'greatest to least']:
                return assert_type
            else:
                print(f'Invalid sorting option: "{assert_type}"')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
