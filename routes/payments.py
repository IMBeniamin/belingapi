from globals import transaction
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/payments",
)


@router.get("/")
async def get_payments():
    data = transaction("select id, customer, invoice, processor, amount, registration, description from payment",
                       fetchall=True)
    return {
        "data": [dict(zip(['id', 'customer', 'invoice', 'processor', 'amount', 'registration', 'description'], item))
                 for item in data]}


@router.get("/{payment_id}")
async def get_payment(payment_id: int):
    data = transaction("select id, customer, invoice, processor, amount, registration, description "
                       "from payment "
                       "where id = %s",
                       [payment_id],
                       fetchall=False)
    return dict(zip(['id', 'customer', 'invoice', 'processor', 'amount', 'registration', 'description'], data)) \
        if data else {"detail": "Invalid SSN"}
