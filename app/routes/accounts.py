from app.globals import transaction
from fastapi import APIRouter
import os

router = APIRouter(
    prefix="/accounts",
)


@router.get("/")
async def get_accounts(key: str):
    if key != os.environ.get("API_KEY"):
        return {"detail": "Unauthorized! Invalid API key"}
    data = transaction("select id, email, pass, creation, deletion, price, website from account",
                       fetchall=True)
    return {"data": [dict(zip(['id', 'email', 'pass', 'creation', 'deletion', 'price', 'website'], item))
                     for item in data]}


@router.get("/{account_id}")
async def get_account(account_id: int, key: str):
    if key != os.environ.get("API_KEY"):
        return {"detail": "Unauthorized! Invalid API key"}
    data = transaction("select id, email, pass, creation, deletion, price, website from account where id = %s",
                       [account_id],
                       fetchall=False)
    return dict(zip(['id', 'email', 'pass', 'creation', 'deletion', 'price', 'website'], data)) \
        if data else {"detail": "Invalid account id"}
