from nis import match
from app.db import MockDB

db = MockDB.db


def get_matches_by_user(user_id):

    if user_id:
        return db[user_id]

    return [*db.values()]


def get_matches_by_org(org_name):
    all_orgs = {}

    for user in db.values():
        matches = user.get("matches", [])

        for opportunity in matches:

            organization = opportunity.get("org_name", "")
            role = opportunity.get("role", "")
            user_interest = opportunity.get("user_interest", "")
            match_level = opportunity.get("match_level", -1)

            wanted = ("user_id", "first_name", "last_name", "email", "user_image")

            new_user = {k: user[k] for k in wanted}
            new_user["match_level"] = match_level
            new_user["user_interest"] = user_interest
            new_user["matching_role"] = role

            if organization not in all_orgs:
                all_orgs[organization] = {
                    "org_name": organization,
                    "roles": [],
                    "matches": [],
                }

            all_orgs[organization]["roles"].append(role)
            all_orgs[organization]["matches"].append(new_user)
            break

    if org_name:
        return all_orgs[org_name]

    return [*all_orgs.items()]
