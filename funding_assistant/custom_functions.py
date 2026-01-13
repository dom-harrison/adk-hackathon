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


def get_savings_account():
        """
        Fetches all savings products a customer is eligible for.

        Returns:
                A json array of product information
        """

        # NOTE: This function returns mock savings account.
        account_type = [
            {
                "account_name": "Fixed Saver 1 year",
                "description": "No withdrawal before enddate",
                "rate": 4.50,
                "age": "18 and above",
                "term": "1 year"
            },
            {
                "account_name": "Fixed Saver 2 year",
                "description": "No withdrawal before enddate",
                "rate": 4.25,
                "age": "18 and above",
                "term": "2 year"
            },
            {
                "account_name": "Fixed Saver 5 year",
                "description": "No withdrawal before enddate",
                "rate": 4.10,
                "age": "18 and above",
                "term": "5 year"
            },
            {
                "account_name": "Easy Saver",
                "description": "Withdraw any time",
                "rate": 1.50,
                "age": "18 and above",
                "term": "1 year"
            },
            {
                "account_name": "Child Saver",
                "description": "Withdraw any time",
                "rate": 1.50,
                "age": "16 and below",
                "term": "Until child turns 18"

            }
        ]
        return account_type