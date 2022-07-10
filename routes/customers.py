from globals import transaction
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/customers",
)


@router.get("/")
async def get_customers():
    data = transaction("select ssn, surname, fullname, email from customer",
                       fetchall=True)
    return {"data": [dict(zip(['ssn', 'surname', 'fullname', 'email'], item)) for item in data]}


@router.get("/{customer_ssn}")
async def get_customer(customer_ssn: str):
    data = transaction("select ssn, surname, fullname, email from customer where ssn = %s",
                       [customer_ssn],
                       fetchall=False)
    return dict(zip(['ssn', 'surname', 'fullname', 'email'], data)) if data else {"detail": "Invalid SSN"}
