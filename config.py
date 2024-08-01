
QUOTE_API = 'https://on-ramp.api.cx.metamask.io'
PROVIDERS = "/providers"
QUOTE_ENDPOINT = "/providers/all/quote"
RANKINGS = "/providers/all/rankings"


REGIONS_API = 'https://on-ramp-content.api.cx.metamask.io/regions/'


CRYPTOCURRENCIES = {
    " Ethereum Mainnet": "/currencies/crypto/1/0x0000000000000000000000000000000000000000"
    , "USDT (Ethereum)": "/currencies/crypto/1/0xdac17f958d2ee523a2206206994597c13d831ec7"
    , "USDT (BNB Chain)": "/currencies/crypto/56/0x55d398326f99059ff775485246999027b3197955"
}


PAYMENT_METHODS = {
    "Debit": "/payments/debit-credit-card",
    "SEPA": "/payments/sepa-bank-transfer",
    "Khipu": "/payments/khipu",
    "PSE": "/payments/pse",
    "Faster Payments": "/payments/gbp-bank-transfer",
    "Instant Bank Transfer": "payments/instant-bank-transfer"
}


COUNTRIES_TO_SCRAPE = {
    "US": {
        "region": "/regions/us-fl"
        , "fiat": "/currencies/fiat/usd"
    }
    , "UK": {
        "region": "/regions/gb"
        , "fiat": "/currencies/fiat/gbp"
    }
    , "DE": {
        "region": "/regions/de"
        , "fiat": "/currencies/fiat/eur"
    }
}
