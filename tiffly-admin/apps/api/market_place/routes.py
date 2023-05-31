from apps import app
from apps.api.market_place.controller import (
    get_market_place
)

app.add_url_rule(
    '/market_place/', 'market_place', get_market_place, methods=['GET']
    )