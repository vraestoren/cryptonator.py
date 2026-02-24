# cryptonator.py
Web-API for [cryptonator.com](https://www.cryptonator.com) website which is an all-in-one online cryptocurrency wallet that supports multiple cryptocurrencies

## Example
```python
from cryptonator import Cryptonator

cryptonator = Cryptonator()
currencies = cryptonator.get_currencies()
print(currencies)
```
