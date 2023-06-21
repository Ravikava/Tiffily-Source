from apps import app
from apps.api.market_place.controller import (
    get_market_place,todo_user_notes,todo_categories
)

app.add_url_rule(
    '/market_place/', 'market_place', get_market_place, methods=['GET']
    )

app.add_url_rule(
    '/todo_user/', 'todo_user', todo_user_notes, methods=['GET']
    )

app.add_url_rule(
    '/get_categories/', 'get_categories', todo_categories, methods=['GET']
    )