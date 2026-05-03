from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.repositories import authenticate_user, create_user, create_user_token, get_user_by_email
from app.db.session import get_db
from app.models.auth import AuthResponse, LoginRequest, RegisterRequest, UserResponse

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(request: RegisterRequest, db: Session = Depends(get_db)) -> UserResponse:
    existing_user = get_user_by_email(db, request.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    user = create_user(db, request)
    return UserResponse(id=user.id, email=user.email)


@router.post("/login", response_model=AuthResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)) -> AuthResponse:
    user = authenticate_user(db, request)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    token = create_user_token(db, user)
    return AuthResponse(access_token=token.token, user=UserResponse(id=user.id, email=user.email))
