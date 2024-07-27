import unittest # Import the Python unit testing framework
import pandas as pd # Import the Pandas library
from io import StringIO  # Import the StringIO module from the io library

# Import the functions from the orders_analysis.py file
from orders_analysis import (add_total_revenue, convert_order_date, calculate_monthly_revenue,
                             calculate_product_revenue, calculate_customer_revenue, top_n_customers)


class TestOrderAnalysis(unittest.TestCase):
    
    def setUp(self):
        # Define the input data for the tests
        data = """order_id,customer_id,order_date,product_id,product_name,product_price,quantity
1,1,2021-01-01,101,Product A,10.0,2
2,1,2021-01-15,102,Product B,20.0,1
3,2,2021-02-01,101,Product A,10.0,1
4,3,2021-02-15,103,Product C,30.0,1
5,2,2021-03-01,102,Product B,20.0,3
"""
        # Create a DataFrame from the input data
        self.df = pd.read_csv(StringIO(data))
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])

    # Define the expected output data for the tests
    def test_add_total_revenue(self):
        df = add_total_revenue(self.df.copy())
        expected_revenue = [20.0, 20.0, 10.0, 30.0, 60.0]
        self.assertListEqual(df['total_revenue'].tolist(), expected_revenue)

    def test_convert_order_date(self):
        df = convert_order_date(self.df.copy())
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df['order_date']))

    def test_calculate_monthly_revenue(self):
        df = add_total_revenue(self.df.copy())
        df = convert_order_date(df)
        monthly_revenue = calculate_monthly_revenue(df)
        expected_monthly_revenue = [40.0, 40.0, 60.0]
        self.assertListEqual(monthly_revenue['total_revenue'].tolist(), expected_monthly_revenue)

    def test_calculate_product_revenue(self):
        df = add_total_revenue(self.df.copy())
        product_revenue = calculate_product_revenue(df)
        expected_product_revenue = {'Product A': 30.0, 'Product B': 80.0, 'Product C': 30.0}
        self.assertEqual(dict(zip(product_revenue['product_name'], product_revenue['total_revenue'])), expected_product_revenue)

    def test_calculate_customer_revenue(self):
        df = add_total_revenue(self.df.copy())
        customer_revenue = calculate_customer_revenue(df)
        expected_customer_revenue = {1: 40.0, 2: 70.0, 3: 30.0}
        self.assertEqual(dict(zip(customer_revenue['customer_id'], customer_revenue['total_revenue'])), expected_customer_revenue)

    def test_top_n_customers(self):
        df = add_total_revenue(self.df.copy())
        top_customers = top_n_customers(df, 2)
        expected_top_customers = {2: 70.0, 1: 40.0}
        self.assertEqual(dict(zip(top_customers['customer_id'], top_customers['total_revenue'])), expected_top_customers)

if __name__ == '__main__':
    unittest.main()