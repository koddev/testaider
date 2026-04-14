from fastapi import APIRouter, HTTPException, status
from app.schemas import ItemCreate, ItemUpdate, ItemResponse
from app import services

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=list[ItemResponse], summary="Tüm öğeleri listele")
async def list_items():
    return services.get_all_items()


@router.get("/{item_id}", response_model=ItemResponse, summary="Öğe detayı")
async def get_item(item_id: int):
    item = services.get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Öğe bulunamadı")
    return item


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED, summary="Yeni öğe oluştur")
async def create_item(data: ItemCreate):
    return services.create_item(data)


@router.put("/{item_id}", response_model=ItemResponse, summary="Öğe güncelle")
async def update_item(item_id: int, data: ItemUpdate):
    item = services.update_item(item_id, data)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Öğe bulunamadı")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Öğe sil")
async def delete_item(item_id: int):
    deleted = services.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Öğe bulunamadı")
