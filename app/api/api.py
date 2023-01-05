from nis import match
from app.db import MockDB
import json 

users = MockDB.users
orgs = MockDB.orgs


def get_matches_by_user(user_id):

    if user_id:
        return users[user_id]

    return [*users.values()]

def get_matches_by_org(org_name):

    if org_name:
        return orgs[org_name]

    return [*orgs.values()]
