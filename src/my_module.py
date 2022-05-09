import re
from datetime import datetime

def is_weekend(client_date):
    date_weekday = datetime.strptime(client_date, "%d%b%Y").weekday()
    return 'weekend' if (date_weekday > 4) else 'weekday'

HOTEL_PRICES_TABLE = {
    'Lakewood': {
        'classification': 3,
        'weekend': {'regular':90, 'reward': 80},
        'weekday': {'regular':110, 'reward': 80}
    },
    'Bridgewood': {
        'classification': 4,
        'weekend': {'regular':60, 'reward': 50},
        'weekday': {'regular':160, 'reward': 110}
    },
    'Ridgewood': {
        'classification': 5,
        'weekend': {'regular':150, 'reward': 40},
        'weekday': {'regular':220, 'reward': 100}
    }
}

def get_cheapest_hotel(data_input):
    DATE_REGEX = r'(\d{1,2}\w{3}\d{4})'

    date_list = re.findall(DATE_REGEX, data_input, re.I)
    client_type = 'regular' if 'regular' in data_input.lower() else 'reward'

    hotel_final_prices = {
        'Lakewood': 0,
        'Bridgewood': 0,
        'Ridgewood': 0
    }

    for client_date in date_list:
        dayweek = is_weekend(client_date)
        for hotel in HOTEL_PRICES_TABLE:
            hotel_price = HOTEL_PRICES_TABLE.get(hotel).get(dayweek).get(client_type) 
            hotel_final_prices[hotel] += hotel_price

    cheaper_price = None
    cheaper_hotel = None

    for hotel in hotel_final_prices:
        hotel_price = hotel_final_prices.get(hotel)
        if (cheaper_price == None) or (hotel_price < cheaper_price) or \
        ((hotel_price == cheaper_price) and (HOTEL_PRICES_TABLE.get(hotel).get('classification') > HOTEL_PRICES_TABLE.get(cheaper_hotel).get('classification'))):
            cheaper_price = hotel_price
            cheaper_hotel = hotel
    
    return cheaper_hotel