from apps import app
from apps.api.restaurants.controller import (
    create_restaurant,get_all_restaurant,testing
)

app.add_url_rule(
    '/create_restaurant/', 'create_restaurant', create_restaurant, methods=['POST']
    )

app.add_url_rule(
    '/get_restaurant/', 'get_restaurant', get_all_restaurant, methods=['GET']
    )

app.add_url_rule(
    '/testing/', 'testing', testing, methods=['GET']
    )