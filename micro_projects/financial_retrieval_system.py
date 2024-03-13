from datetime import (
    date,
    timedelta
)
from dotenv import load_dotenv
import os
import requests
import logging

# Load environment variables from .env file
load_dotenv()
# Set the basic config of the logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s-%(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)


class FinancialDataRetrievalSystem:
    def __init__(
        self,
        currency_api_key: str,
        share_api_key: str,
        days_from_today: int
    ) -> None:

        # Initialize attributes
        self.currency_api_key = currency_api_key
        self.share_api_key = share_api_key
        self.base_url_price: str = "https://api.polygon.io/v2/aggs/ticker/"
        self.base_url_info: str = "https://api.polygon.io/v3/reference/tickers/"
        self.base_url_fmp: str = "https://financialmodelingprep.com/api/v3/stock_market/"
        self.date = date.today() - timedelta(days=days_from_today)

    def get_currency_exchange_rate(
        self,
        base_currency: str,
        target_currency: str
    ) -> float | None:

        self.base_currency = base_currency
        self.target_currency = target_currency
        url = f"{self.base_url_price}C:{self.base_currency.upper()}{self.target_currency.upper()}/range/1/day/{self.date}/{self.date}?apiKey={self.currency_api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            exchange_rate = response.json()["results"]
            return exchange_rate
        else:
            logging.info("404: Finance info not found")
            return None

    def get_company_share_price(
        self,
        company_symbol: str
    ):
        # Retrieve the current price of shares for a given company using the share API

        url = f"{self.base_url_price}{company_symbol.upper()}/range/1/day/{self.date}/{self.date}?apiKey={self.currency_api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            share_price = response.json()["results"]
            return share_price
        else:
            logging.info("404: Finance info not found")
            return None

    def get_currency_conversion(
        self,
        amount: float,
        base_currency: str,
        target_currency: str
    ) -> float:

        # Convert the given amount from one currency to another

        self.target_currency = target_currency
        exchange_rate = self.get_currency_exchange_rate(
            base_currency,
            target_currency
        )

        converted_amount = float(amount) * exchange_rate[0]["c"]

        return converted_amount

    def get_company_info(
        self,
        company_symbol: str
    ):
        # Retrieve additional information about a company (e.g., name, sector) using the share API

        desired_keys = ["name", "market_cap", "description", "sic_description", "homepage_url"]
        url = f"{self.base_url_info}{company_symbol.upper()}?apiKey={self.currency_api_key}"

        response = requests.get(url)

        if response.status_code == 200:
            company_info = response.json()["results"]
            information = []

            selected_data = {key: company_info[key] for key in desired_keys}
            information.append(selected_data)

            information = information[0]

            for key, value in information.items():
                print(f"{key}: {value}\n")

        else:
            logging.error("404: Finance info not found")

    def get_top_gainers(self):
        # Retrieve the top gaining companies from the share API

        gainers_api = f"{self.base_url_fmp}gainers?apikey={self.share_api_key}"
        response = requests.get(gainers_api)

        if response.status_code == 200:
            top_gainers = response.json()
            for company in top_gainers:
                print(company)
        else:
            logging.error("404: Finance info not found")

    def get_top_losers(self):
        # Retrieve the top losing companies from the share API

        losers_api = f"{self.base_url_fmp}losers?apikey={self.share_api_key}"
        response = requests.get(losers_api)

        if response.status_code == 200:
            top_losers = response.json()
            for company in top_losers:
                print(company)
        else:
            logging.error("404: Finance info not found")


if __name__ == "__main__":

    currency_api_key = os.getenv("API_KEY")
    share_api_key = os.getenv("FMP_API_KEY")

    financial_system = FinancialDataRetrievalSystem(
        currency_api_key,
        share_api_key,
        days_from_today=1
    )

    # Call methods of the FinancialDataRetrievalSystem object as needed...
    financial_system.get_currency_exchange_rate("EUR", "BGN")
    financial_system.get_company_share_price("AAPL")
    financial_system.get_currency_conversion(10, "GBP", "USD")
    financial_system.get_company_info("tsla")
    financial_system.get_top_gainers()
    financial_system.get_top_losers()
