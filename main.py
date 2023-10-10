import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from enum import Enum


app = FastAPI()

# load currency data
currencies_json = json.loads(open("currencies.json").read())
currencies = currencies_json["currencies"]

# parameter validation
CurrencyEnum = Enum(
    "CurrencyEnum",
    [(currency, currency) for currency, exchange_rates in currencies.items()],
)


@app.get("/")
def convert_currency(source: CurrencyEnum, target: CurrencyEnum, amount: str):
    exchange_rate = currencies[source.value][target.value]

    # handle invalid ammount
    try:
        int_amount = int(amount.replace(",", "").replace("$", ""))
    except ValueError as e:
        return JSONResponse(
            status_code=400,
            content={"message": str(e)},
        )
    converted_amount = "$" + format(round(exchange_rate * int_amount, 2), ",")

    return JSONResponse(
        status_code=200,
        content={"msg": "success", "amount": converted_amount},
    )
