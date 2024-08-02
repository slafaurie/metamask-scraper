############## REGION - Get Payment
REGION_PARAMS = {
    "sdk":"1.28.3"
}
REGIONS_API = 'https://on-ramp-content.api.cx.metamask.io/regions'
REGIONS = [
    {
        "region":"de"
        , "country":"DE"
        , "fiat_currency": "/currencies/fiat/eur"
    },
    {
        "region":"us-fl"
        , "country":"US"
        , "fiat_currency": "/currencies/fiat/usd"
    },
    {
        "region":"gb"
        , "country":"UK"
        , "fiat_currency": "/currencies/fiat/gb"
    }
]

############## QUOTE
QUOTE_API = 'https://on-ramp.api.cx.metamask.io/providers/all/quote'
CRYPTOCURRENCIES = [
    {
        "name": "Ethereum Mainnet"
        , "id": "/currencies/crypto/1/0x0000000000000000000000000000000000000000"
    },
    {
        "name": "USDT (Ethereum)"
        , "id":  "/currencies/crypto/1/0xdac17f958d2ee523a2206206994597c13d831ec7"
    },
    {
        "name": "USDT (BNB Chain)"
        , "id":  "/currencies/crypto/56/0x55d398326f99059ff775485246999027b3197955"
    },
    
]