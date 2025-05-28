from fastapi import APIRouter
from models import (supplier_pydantic, supplier_pydanticIn, Supplier)



router = APIRouter(
    prefix="/supplier",
    tags=["supplier"]
)

@router.post('/')
async def add_supplier(supplier_info: supplier_pydanticIn):
    supplier_obj = await Supplier.create(**supplier_info.dict(exclude_unset=True))
    response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
    return {'status':'ok', 'data':response}

@router.get('/')
async def get_all_supplier():
    response = await supplier_pydantic.from_queryset(Supplier.all())
    return {'status':'ok', 'data':response}

@router.get('/{supplier_id}')
async def get_one_supplier(supplier_id: int):
    response = await supplier_pydantic.from_queryset_single(Supplier.get(id=supplier_id))
    return {'status':'ok', 'data':response}

@router.put('/{supplier_id}')
async def update_supplier(supplier_id: int, update_info:supplier_pydanticIn):
    supplier = await Supplier.get(id = supplier_id)
    update_info = update_info.dict(exclude_unset=True)
    supplier.name = update_info['name']
    supplier.company = update_info['company']
    supplier.email = update_info['email']
    supplier.phone = update_info['phone']
    await supplier.save()
    response = await supplier_pydantic.from_tortoise_orm(supplier)
    return {'status':'ok', 'data':response}

@router.delete('/{supplier_id}')
async def delete_supplier(supplier_id: int):
    await Supplier.get(id = supplier_id).delete()
    return {'status':'ok'}