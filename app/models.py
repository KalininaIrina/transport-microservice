from pydantic import BaseModel, Field


class RouteBase(BaseModel):
    name: str = Field(..., description="Название маршрута")
    start_point: str = Field(..., description="Точка отправления")
    end_point: str = Field(..., description="Точка прибытия")
    distance_km: float = Field(..., gt=0, description="Расстояние в км")


class RouteCreate(RouteBase):
    pass


class RouteResponse(RouteBase):
    id: int = Field(..., description="Уникальный идентификатор")
