from globals import transaction
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/surpluses",
)


@router.get("/")
async def get_surpluses():
    data = transaction("select customer, amount from surplus",
                       fetchall=True)
    return {"data": [dict(zip(['customer', 'amount'], item))
                     for item in data]}


@router.get("/{customer_ssn}")
async def get_surplus(customer_ssn: str):
    data = transaction("select customer, amount from surplus where customer = %s",
                       [customer_ssn],
                       fetchall=False)
    return dict(zip(['customer', 'amount'], data)) if data else {
        "detail": "Invalid SSN"}
