from apps import app
from apps.api.users.controller import (
    create_user,get_user,profile_update,authenticate_user
)

app.add_url_rule('/create_user/', 'create_user',
                 create_user, methods=['POST'])


app.add_url_rule('/get_user/', 'get_user',
                 get_user, methods=['GET'])

app.add_url_rule('/profile_update/', 'profile_update',
                 profile_update, methods=['POST'])

app.add_url_rule('/authenticate_user/', 'authenticate_user',
                 authenticate_user, methods=['POST'])