from typing import List
from models import product_pydantic, Product, product_pydanticin, Supplier
from fastapi import BackgroundTasks, FastAPI, APIRouter, HTTPException
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from dotenv import dotenv_values
from tortoise.exceptions import DoesNotExist
import traceback  

router = APIRouter(
    prefix="/email",
    tags=["email"]
)
credentials = dotenv_values(".env")


class EmailSchema(BaseModel):
    email: List[EmailStr]

class EmailContent(BaseModel):
    message : str
    subject : str

conf = ConnectionConfig(
    MAIL_USERNAME = credentials['MAIL_USERNAME'],
    MAIL_PASSWORD = credentials['MAIL_PASSWORD'],
    MAIL_FROM = credentials['MAIL_USERNAME'],
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


@router.post('/email/{product_id}')
async def send_email(product_id: int, content: EmailContent):
    try:
        product = await Product.get(id=product_id) 
        supplier = await product.supplied_by
        
        if not supplier or not supplier.email:
            raise HTTPException(status_code=400, detail="Supplier or supplier email not found.")

        supplier_email = [supplier.email]

        html = f"""
        <p>John Doe Business LTD</p>
        <br>
        <p>{content.message}</p> 
        <br>
        <h6>Best Regards</h6>
        <h6>John Doe LTD</h6>
        """

        message = MessageSchema(
            subject=content.subject,
            recipients=supplier_email,
            body=html,
            subtype=MessageType.html
        )

        fm = FastMail(conf)
        await fm.send_message(message)

        return JSONResponse(status_code=200, content={"message": "Email has been sent"})

    except DoesNotExist: 
        raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
