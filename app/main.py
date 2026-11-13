from fastapi import FastAPI, HTTPException, status
from app.models import RouteCreate, RouteResponse

app = FastAPI(
    title="Transport Microservice API",
    description="API для управления маршрутами",
    version="1.0.0"
)

# In-Memory хранилище (заглушка)
routes_db: dict[int, dict] = {}
current_id = 1


@app.get(
    "/api/v1/routes/",
    response_model=list[RouteResponse],
    status_code=status.HTTP_200_OK,
    summary="Получить список всех маршрутов"
)
async def get_routes():
    return list(routes_db.values())


@app.get(
    "/api/v1/routes/{route_id}",
    response_model=RouteResponse,
    status_code=status.HTTP_200_OK,
    responses={404: {"description": "Маршрут не найден"}},
    summary="Получить маршрут по ID"
)
async def get_route(route_id: int):
    if route_id not in routes_db:
        raise HTTPException(status_code=404, detail="Route not found")
    return routes_db[route_id]


@app.post(
    "/api/v1/routes/",
    response_model=RouteResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"description": "Невалидные данные"}},
    summary="Создать новый маршрут"
)
async def create_route(route: RouteCreate):
    global current_id
    new_route = {"id": current_id, **route.model_dump()}
    routes_db[current_id] = new_route
    current_id += 1
    return new_route


@app.delete(
    "/api/v1/routes/{route_id}",
    status_code=status.HTTP_200_OK,
    responses={404: {"description": "Маршрут не найден"}},
    summary="Удалить маршрут"
)
async def delete_route(route_id: int):
    if route_id not in routes_db:
        raise HTTPException(status_code=404, detail="Route not found")
    del routes_db[route_id]
    return {"message": "Route deleted successfully"}
