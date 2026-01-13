import requests

# define a function to get exchange rate
def get_fx_rate(base: str, target: str):
        """
        Fetches the current exchange rate between two currencies.

        Args:
                base: The base currency (e.g., "SGD").
                target: The target currency (e.g., "JPY").

        Returns:
                The exchange rate information as a json response,
                or None if the rate could not be fetched.
        """
        base_url = "https://hexarate.paikama.co/api/rates/latest"
        api_url = f"{base_url}/{base}?target={target}"

        response = requests.get(api_url)
        if response.status_code == 200:
                return response.json()


def get_transaction_history(partyId: str):
        """
        Fetches transaction history for a given party ID.

        Args:
                partyId: The party ID for which to fetch transaction history.


        Returns:
                A json array of account transactions
        """
        
        # NOTE: This function returns mock data and ignores the partyId for now.
        transactions = [
            # October 2023
            { "transaction_id": "txn_1001", "date": "2023-10-28T09:00:00Z", "description": "Monthly Salary", "amount": 2500.00, "currency": "GBP", "type": "credit", "category": "Income" },
            { "transaction_id": "txn_1002", "date": "2023-10-26T10:30:00Z", "description": "Starbucks", "amount": 4.50, "currency": "GBP", "type": "debit", "category": "Food & Drink" },
            { "transaction_id": "txn_1003", "date": "2023-10-25T14:15:22Z", "description": "Amazon.com", "amount": 38.99, "currency": "GBP", "type": "debit", "category": "Shopping" },
            { "transaction_id": "txn_1004", "date": "2023-10-23T11:00:00Z", "description": "Tesco Groceries", "amount": 75.50, "currency": "GBP", "type": "debit", "category": "Groceries" },
            { "transaction_id": "txn_1005", "date": "2023-10-22T18:45:00Z", "description": "Transport for London", "amount": 15.80, "currency": "GBP", "type": "debit", "category": "Transport" },
            { "transaction_id": "txn_1006", "date": "2023-10-20T08:00:00Z", "description": "Pret a Manger", "amount": 7.80, "currency": "GBP", "type": "debit", "category": "Food & Drink" },
            { "transaction_id": "txn_1007", "date": "2023-10-15T13:00:00Z", "description": "Sainsbury's Groceries", "amount": 62.30, "currency": "GBP", "type": "debit", "category": "Groceries" },
            { "transaction_id": "txn_1008", "date": "2023-10-12T17:00:00Z", "description": "Cineworld", "amount": 12.50, "currency": "GBP", "type": "debit", "category": "Entertainment" },
            { "transaction_id": "txn_1009", "date": "2023-10-10T09:00:00Z", "description": "Netflix Subscription", "amount": 10.99, "currency": "GBP", "type": "debit", "category": "Bills" },
            { "transaction_id": "txn_1010", "date": "2023-10-08T10:00:00Z", "description": "Gym Membership", "amount": 35.00, "currency": "GBP", "type": "debit", "category": "Health & Wellness" },
            { "transaction_id": "txn_1011", "date": "2023-10-05T09:00:00Z", "description": "Phone Bill", "amount": 40.00, "currency": "GBP", "type": "debit", "category": "Bills" },
            { "transaction_id": "txn_1012", "date": "2023-10-01T09:00:00Z", "description": "Rent", "amount": 1200.00, "currency": "GBP", "type": "debit", "category": "Housing" },

            # September 2023
            { "transaction_id": "txn_2001", "date": "2023-09-28T09:00:00Z", "description": "Monthly Salary", "amount": 2500.00, "currency": "GBP", "type": "credit", "category": "Income" },
            { "transaction_id": "txn_2002", "date": "2023-09-26T12:00:00Z", "description": "ASOS", "amount": 55.00, "currency": "GBP", "type": "debit", "category": "Shopping" },
            { "transaction_id": "txn_2003", "date": "2023-09-24T19:00:00Z", "description": "Nando's", "amount": 25.50, "currency": "GBP", "type": "debit", "category": "Food & Drink" },
            { "transaction_id": "txn_2004", "date": "2023-09-21T20:00:00Z", "description": "Concert Tickets", "amount": 75.00, "currency": "GBP", "type": "debit", "category": "Entertainment" },
            { "transaction_id": "txn_2005", "date": "2023-09-18T11:00:00Z", "description": "Lidl Groceries", "amount": 45.20, "currency": "GBP", "type": "debit", "category": "Groceries" },
            { "transaction_id": "txn_2006", "date": "2023-09-17T17:00:00Z", "description": "Haircut", "amount": 30.00, "currency": "GBP", "type": "debit", "category": "Personal Care" },
            { "transaction_id": "txn_2007", "date": "2023-09-14T11:00:00Z", "description": "Book Store", "amount": 25.00, "currency": "GBP", "type": "debit", "category": "Shopping" },
            { "transaction_id": "txn_2008", "date": "2023-09-11T19:00:00Z", "description": "Pub Drinks", "amount": 20.00, "currency": "GBP", "type": "debit", "category": "Food & Drink" },
            { "transaction_id": "txn_2009", "date": "2023-09-10T09:00:00Z", "description": "Netflix Subscription", "amount": 10.99, "currency": "GBP", "type": "debit", "category": "Bills" },
            { "transaction_id": "txn_2010", "date": "2023-09-08T10:00:00Z", "description": "Gym Membership", "amount": 35.00, "currency": "GBP", "type": "debit", "category": "Health & Wellness" },
            { "transaction_id": "txn_2011", "date": "2023-09-05T09:00:00Z", "description": "Phone Bill", "amount": 40.00, "currency": "GBP", "type": "debit", "category": "Bills" },
            { "transaction_id": "txn_2012", "date": "2023-09-01T09:00:00Z", "description": "Rent", "amount": 1200.00, "currency": "GBP", "type": "debit", "category": "Housing" },

            # August 2023
            { "transaction_id": "txn_3001", "date": "2023-08-28T09:00:00Z", "description": "Monthly Salary", "amount": 2500.00, "currency": "GBP", "type": "credit", "category": "Income" },
            { "transaction_id": "txn_3002", "date": "2023-08-29T19:30:00Z", "description": "Restaurant Dinner", "amount": 65.00, "currency": "GBP", "type": "debit", "category": "Food & Drink" },
            { "transaction_id": "txn_3003", "date": "2023-08-26T15:00:00Z", "description": "Zara", "amount": 89.99, "currency": "GBP", "type": "debit", "category": "Shopping" },
            { "transaction_id": "txn_3004", "date": "2023-08-22T10:00:00Z", "description": "Pharmacy", "amount": 12.75, "currency": "GBP", "type": "debit", "category": "Health & Wellness" },
            { "transaction_id": "txn_3005", "date": "2023-08-20T15:00:00Z", "description": "Holiday Spending", "amount": 300.00, "currency": "GBP", "type": "debit", "category": "Travel" },
            { "transaction_id": "txn_3006", "date": "2023-08-19T13:00:00Z", "description": "Waitrose Groceries", "amount": 88.40, "currency": "GBP", "type": "debit", "category": "Groceries" },
            { "transaction_id": "txn_3007", "date": "2023-08-15T11:00:00Z", "description": "Petrol Station", "amount": 50.00, "currency": "GBP", "type": "debit", "category": "Transport" },
            { "transaction_id": "txn_3008", "date": "2023-08-13T10:00:00Z", "description": "Internet Bill", "amount": 35.00, "currency": "GBP", "type": "debit", "category": "Bills" },
            { "transaction_id": "txn_3009", "date": "2023-08-10T09:00:00Z", "description": "Netflix Subscription", "amount": 10.99, "currency": "GBP", "type": "debit", "category": "Bills" },
            { "transaction_id": "txn_3010", "date": "2023-08-08T10:00:00Z", "description": "Gym Membership", "amount": 35.00, "currency": "GBP", "type": "debit", "category": "Health & Wellness" },
            { "transaction_id": "txn_3011", "date": "2023-08-05T09:00:00Z", "description": "Phone Bill", "amount": 40.00, "currency": "GBP", "type": "debit", "category": "Bills" },
            { "transaction_id": "txn_3012", "date": "2023-08-01T09:00:00Z", "description": "Rent", "amount": 1200.00, "currency": "GBP", "type": "debit", "category": "Housing" }
        ]
        return transactions


def get_savings_account():
        """
        Fetches all savings products a customer is eligible for.

        Returns:
                A json array of product information
        """

        # NOTE: This function returns mock savings account.
        account_type = [
            {
                "account_name": "Fixed Saver",
                "description": "No withdrawal before enddate",
                "rate": 4.50,
                "age": "18 and above"
            },
            {
                "account_name": "Easy Saver",
                "description": "Withdraw any time",
                "rate": 1.50,
                "age": "18 and above"
            },
            {
                "account_name": "Child Saver",
                "description": "Withdraw any time",
                "rate": 1.50,
                "age": "16 and below"

            }
        ]
        return account_type