from fastapi import APIRouter, HTTPException
from models import product_pydantic, Product, product_pydanticin, Supplier
from tortoise.exceptions import DoesNotExist


router = APIRouter(
    prefix="/product",
    tags=["product"]
)

@router.post("/{supplier_id}")
async def add_product(supplier_id: int,product_info: product_pydanticin):
    supplier = await Supplier.get(id=supplier_id)
    product_info = product_info.dict(exclude_unset=True)
    product_info['revenue'] += product_info['quantity_sold'] * product_info['unit_price']
    product_obj = await Product.create(**product_info, supplied_by = supplier)
    response = await product_pydantic.from_tortoise_orm(product_obj)
    return {'status':'ok', 'data':response}

@router.get('/')
async def all_products():
    try:
        response = await product_pydantic.from_queryset(Product.all())
        return {'status':'ok', 'data':response}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail='Product not found')  

@router.get('/{id}')
async def one_products(id: int):
    try:
        product = await Product.get(id=id)
        response = await product_pydantic.from_tortoise_orm(product)
        return {'status': 'ok', 'data': response}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail='Product not found')


@router.put('/{id}')
async def update_product(id: int, update_info:product_pydanticin):
    try:
        product = await Product.get(id=id)
        update_info = update_info.dict(exclude_unset=True)
        product.name = update_info['name']
        product.quantity_in_stack = update_info['quantity_in_stack']
        product.quantity_sold = update_info['quantity_sold']
        product.unit_price = update_info['unit_price']
        product.revenue += update_info['quantity_sold']*update_info['unit_price']
        await product.save()
        response = await product_pydantic.from_tortoise_orm(product)
        return {'status':'ok', 'data':response}
    except DoesNotExist:
        raise HTTPException(status_code=400, detail='error')

@router.delete('/{id}')
async def delet_product(id: int):
    await Product.filter(id=id).delete()
    return {'status':'ok'}

