from pydantic import BaseModel

class SprayRequest(BaseModel):
    action: str    # "spray" | "stop"
    duration: int  # seconds

class RobotStatus(BaseModel):
    spraying: bool
    battery: int   # percentage
    solar: int     # percentage
