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
            {
                "transaction_id": "txn_12345",
                "date": "2023-10-26T10:30:00Z",
                "description": "Starbucks",
                "amount": 4.50,
                "currency": "GBP",
                "type": "debit",
                "category": "Food & Drink"
            },
            {
                "transaction_id": "txn_12346",
                "date": "2023-10-25T14:15:22Z",
                "description": "Amazon.com",
                "amount": 38.99,
                "currency": "GBP",
                "type": "debit",
                "category": "Shopping"
            },
            {
                "transaction_id": "txn_12347",
                "date": "2023-10-22T09:00:00Z",
                "description": "Monthly Salary",
                "amount": 2500.00,
                "currency": "GBP",
                "type": "credit",
                "category": "Income"
            },
            {
                "transaction_id": "txn_12348",
                "date": "2023-10-20T11:00:00Z",
                "description": "Tesco Groceries",
                "amount": 75.50,
                "currency": "GBP",
                "type": "debit",
                "category": "Groceries"
            },
            {
                "transaction_id": "txn_12349",
                "date": "2023-10-18T18:45:00Z",
                "description": "Transport for London",
                "amount": 15.80,
                "currency": "GBP",
                "type": "debit",
                "category": "Transport"
            }
        ]
        return transactions


def get_savings_account():
        """
        Fetches all the savings account.

        Returns:
                A json array of account information
        """

        # NOTE: This function returns mock savings account.
        account_type = [
            {
                "account_name": "Fixed Saver",
                "description": "Withdraw any time",
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