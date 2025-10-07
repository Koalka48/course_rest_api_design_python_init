from ninja import Router
from api.schemas.bark_schemas import BarkSchemaOut
from api.schemas.bark_schemas import ErrorSchemaOut
from api.schemas.bark_schemas import BarkSchemaIn
from core.models import BarkModel
from uuid import UUID

router = Router()


@router.get("/{bark_id}/", response={200: BarkSchemaOut, 404: ErrorSchemaOut})
def barks_list(request, bark_id: int):
    """
    Bark list endpoint that returns a list of barks.
    """
    try:
        bark = BarkModel.objects.get(id=bark_id)
        return bark
    except BarkModel.DoesNotExist:
        return 404, {"error": "Bark not found"}


@router.get("/{bark_id}/", response={200: BarkSchemaOut, 404: ErrorSchemaOut})
def get_bark(request, bark_id: int):
    """
    Bark detail endpoint that returns a single bark.
    """
    if bark_id in range (1, 4):
        return 200, {"id": bark_id, "message": f"bark {bark_id}!", "breed": "Poodle"}
    return 404, {"error": "Bark not found"}

@router.delete("/{bark_id}/", response={204: None, 404: ErrorSchemaOut})
def delete_bark(request, bark_id: int):
    if bark_id in range (1, 4):
        return 204, None
    return 404, {"error": "Bark not found"}

@router.put("/{bark_id}/", response={200: BarkSchemaOut, 404: ErrorSchemaOut})
def update_bark(request, bark_id: int, bark: BarkSchemaIn):
    """Update an existing bark."""
    if bark_id in range (1, 4):
        return 200, {"id": bark_id, "message": bark.message}
    return 404, {"error": "Bark not found"}