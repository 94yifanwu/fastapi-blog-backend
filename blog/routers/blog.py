from fastapi import APIRouter, Depends, status
from .. import database, schemas, oauth2
from sqlalchemy.orm import Session
from ..repository import blog
from typing import List

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlogResponse])
def all(current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlogResponse)
def show(id: int, request: schemas.Blog, current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return blog.show(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    # add user id
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return blog.update(id, request, db)
