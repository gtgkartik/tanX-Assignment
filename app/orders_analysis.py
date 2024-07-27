import pandas as pd

# the below function will load the csv file 
def load_data(file_path):
    return pd.read_csv(file_path)

# takes the dataframe and give the output of total revenue
def add_total_revenue(df):
    df['total_revenue'] = df['product_price'] * df['quantity']
    return df

# convert the order date to datetime format
def convert_order_date(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df

# calculate the monthly revenue
def calculate_monthly_revenue(df):
    df['month'] = df['order_date'].dt.to_period('M')
    monthly_revenue = df.groupby('month')['total_revenue'].sum().reset_index()
    return monthly_revenue

# calculate the product revenue
def calculate_product_revenue(df):
    product_revenue = df.groupby('product_name')['total_revenue'].sum().reset_index()
    return product_revenue

# calculate the customer revenue
def calculate_customer_revenue(df):
    customer_revenue = df.groupby('customer_id')['total_revenue'].sum().reset_index()
    return customer_revenue

# calculate the top n customers
def top_n_customers(df, n=10):
    customer_revenue = calculate_customer_revenue(df)
    top_customers = customer_revenue.sort_values(by='total_revenue', ascending=False).head(n)
    return top_customers

# main function to call all the functions
def main(file_path):
    df = load_data(file_path) # load the data
    df = add_total_revenue(df) # add the total revenue
    df = convert_order_date(df) # convert the order date to datetime format

    monthly_revenue = calculate_monthly_revenue(df) 
    product_revenue = calculate_product_revenue(df)
    customer_revenue = calculate_customer_revenue(df)
    top_10_customers = top_n_customers(df)

 # print the output results
    print("Monthly Revenue:\n", monthly_revenue)
    print("\nProduct Revenue:\n", product_revenue)
    print("\nCustomer Revenue:\n", customer_revenue)
    print("\nTop 10 Customers:\n", top_10_customers)

# main function to call the main function
if __name__ == "__main__":
    main('orders.csv')
