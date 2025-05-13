

from fastapi import APIRouter, Depends   # ← APIRouter ve Depends import et
from app.core.security import get_current_user
from app.db.models       import User
from app.models.user     import UserRead


router = APIRouter(tags=["users"])

@router.get("/me", response_model=UserRead)
def read_users_me(
    current_user: User = Depends(get_current_user)
):
    """
    Şu an token ile oturum açmış kullanıcı bilgisini döner.
    """
    return current_user
