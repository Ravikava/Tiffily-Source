from apps import app
from apps.api.restaurants.controller import (
    create_restaurant,get_all_restaurant,
    testing,add_menu_item,get_menu_item,
    edit_menu_item,delete_menu_item
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

app.add_url_rule(
    '/add_menu_item/', 'add_menu_item', add_menu_item, methods=['POST']
    )

app.add_url_rule(
    '/get_menu_item/', 'get_menu_item', get_menu_item, methods=['GET']
    )

app.add_url_rule(
    '/edit_menu_item/', 'edit_menu_item', edit_menu_item, methods=['GET','POST']
    )

app.add_url_rule(
    '/delete_menu_item/<int:id>', 'delete_menu_item', delete_menu_item, methods=['POST']
    )