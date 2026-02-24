from requests import Session

class Cryptonator:
	def __init__(self) -> None:
		self.api = "https://api.cryptonator.com/api"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_currencies(self) -> dict:
		return self.session.get(f"{self.api}/currencies").json()

	def get_simple_ticker(self, currency_code: str) -> dict:
		return self.session.get(f"{self.api}/ticker/{currency_code}").json()

	def get_complete_ticker(self, currency_code: str) -> dict:
		return self.session.get(f"{self.api}/full/{currency_code}").json()	
