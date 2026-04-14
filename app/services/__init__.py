from typing import Optional
from app.schemas import ItemCreate, ItemUpdate, ItemResponse

# Basit in-memory veri deposu
_items: dict[int, dict] = {}
_counter: int = 0


def get_all_items() -> list[ItemResponse]:
    return [ItemResponse(id=k, **v) for k, v in _items.items()]


def get_item_by_id(item_id: int) -> Optional[ItemResponse]:
    item = _items.get(item_id)
    if item is None:
        return None
    return ItemResponse(id=item_id, **item)


def create_item(data: ItemCreate) -> ItemResponse:
    global _counter
    _counter += 1
    _items[_counter] = data.model_dump()
    return ItemResponse(id=_counter, **_items[_counter])


def update_item(item_id: int, data: ItemUpdate) -> Optional[ItemResponse]:
    if item_id not in _items:
        return None
    update_data = data.model_dump(exclude_unset=True)
    _items[item_id].update(update_data)
    return ItemResponse(id=item_id, **_items[item_id])


def delete_item(item_id: int) -> bool:
    if item_id not in _items:
        return False
    del _items[item_id]
    return True
