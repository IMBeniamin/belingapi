from globals import transaction
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/accounts",
)


@router.get("/")
async def get_accounts():
    data = transaction("select id, email, pass, creation, deletion, price, website from account",
                       fetchall=True)
    return {"data": [dict(zip(['id', 'email', 'pass', 'creation', 'deletion', 'price', 'website'], item))
                         for item in data]}


@router.get("/{account_id}")
async def get_account(account_id: int):
    data = transaction("select id, email, pass, creation, deletion, price, website from account where id = %s",
                       [account_id],
                       fetchall=False)
    return dict(zip(['id', 'email', 'pass', 'creation', 'deletion', 'price', 'website'], data)) \
        if data else {"detail": "Invalid account id"}
