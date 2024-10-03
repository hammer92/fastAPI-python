
from fastapi import FastAPI, Depends
from typing_extensions import Annotated

from core.entities.config import get_environment_variables, EnvironmentSettings
from infra.api.fastapi.routers.owner_router import OwnerRouter

env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION
)

# Add Routers
app.include_router(OwnerRouter)

@app.get("/info")
async def info(settings: Annotated[EnvironmentSettings, Depends(get_environment_variables)]):
    return {
        "app_name": settings.APP_NAME,
        "debug_mode": settings.DEBUG_MODE,
        "api_version": settings.API_VERSION,
    }
