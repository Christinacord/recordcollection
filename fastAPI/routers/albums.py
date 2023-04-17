from fastAPI import (
    Depends,
    HTTPException,
    status,
    APIRouter,
)
from pydantic import BaseModel
from authenticator import authenticator
from typing import Optional
from queries.albums import DuplicateAlbumError, AlbumIn, AlbumOut, AlbumQueries


class AlbumForm(BaseModel):
    album_name: str


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.get("/api/albums/{id}")
async def get_album(id: int, repo: AlbumQueries = Depends()):
    account_data: Optional[dict] = (
        Depends(authenticator.try_get_current_account_data),
    )
    if account_data:
        album = repo.get_by_id(id)
        if album is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Album not found"
            )
        return album


@router.get("/api/albums", response_model=list[AlbumOut])
async def get_albums(repo: AlbumQueries = Depends()):
    account_data: Optional[dict] = (
        Depends(authenticator.try_get_current_account_data),
    )
    if account_data:
        return repo.get_all_albums()
