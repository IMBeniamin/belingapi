from globals import transaction
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/invoices",
)


@router.get("/")
async def get_invoices():
    data = transaction("select id, emission, customer, account, paid, expiry, amount from invoice",
                       fetchall=True)
    return {"data": [dict(zip(['id', 'emission', 'customer', 'account', 'paid', 'expiry', 'amount'], item))
                         for item in data]}


@router.get("/{invoice_id}")
async def get_invoice(invoice_id: str):
    data = transaction("select id, emission, customer, account, paid, expiry, amount from invoice where id = %s",
                       [invoice_id],
                       fetchall=False)
    return dict(zip(['id', 'emission', 'customer', 'account', 'paid', 'expiry', 'amount'], data)) if data else {"detail": "Invalid SSN"}
