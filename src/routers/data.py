from fastapi import APIRouter, HTTPException
from src.models import DataModel

router = APIRouter(prefix='/data', tags=['data'])

@router.get('/')
def read_data():
    return [{'id': 1, 'name': 'Sample Data'}]
