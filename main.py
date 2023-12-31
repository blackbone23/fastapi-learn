from fastapi import FastAPI
from fastapi.responses import JSONResponse
from users.routes import router as guest_router
from users.routes import user_router as user_router
from auth.routes import router as auth_router
from core.security import JWTAuth
from starlette.middleware.authentication import AuthenticationMiddleware
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app = FastAPI()
app.include_router(guest_router)
app.include_router(user_router)
app.include_router(auth_router)

# middleware 
app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get('/')
def health_check():
  return JSONResponse(content={'status': 'Running!'})