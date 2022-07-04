import uuid
from fastapi import FastAPI

from app.config import description, tags_metadata
from app.api import api

app = FastAPI(
    title="Opportunity Match Server",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata,
)

serverID = uuid.uuid4()


def _paginate(data, page_num, page_size):
    """Helper to create pagination resp"""
    data_length = len(data)
    start = (page_num - 1) * page_size
    end = start + page_size

    resp = {
        "data": data[start:end],
        "total": len(data),
        "count": page_size,
        "pagination": {},
    }

    if end >= data_length:
        resp["pagination"]["next"] = None

        if page_num > 1:
            resp["pagination"][
                "previous"
            ] = f"/matches?page_num={page_num-1}&page_size={page_size}"
        else:
            resp["pagination"]["previous"] = None
    else:
        if page_num > 1:
            resp["pagination"][
                "previous"
            ] = f"/matches?page_num={page_num-1}&page_size={page_size}"
        else:
            resp["pagination"]["previous"] = None

        resp["pagination"][
            "next"
        ] = f"/matches?page_num={page_num+1}&page_size={page_size}"

    return resp


# ROOT / HEARTBEAT ENDPOINT
@app.get("/", tags=["server"])
def check_server():
    # Root method that just returns a heartbeat
    return {"message": "Fast API Server", "server_id": serverID}


# Matches / Get matches
@app.get(
    "/matches_by_user/",
    tags=["matches"],
    description="Returns matches by user. Not specifiying a userId returns all users",
)
async def get_matches_by_user(
    user_id: str = None, page_num: int = 1, page_size: int = 10
):
    data = api.get_matches_by_user(user_id)

    if user_id:
        return data

    return _paginate(data, page_num, page_size)


@app.get(
    "/matches_by_org/",
    tags=["matches"],
    description="Returns matches by organization. Not specifiying an organization name returns all organizations",
)
async def get_matches_by_org(
    org_name: str = None, page_num: int = 1, page_size: int = 10
):
    data = api.get_matches_by_org(org_name)

    if org_name:
        return data

    return _paginate(data, page_num, page_size)
