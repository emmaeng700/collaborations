from fastapi import APIRouter

router = APIRouter(prefix="/robot", tags=["Robot"])

# TODO (Akontoke): POST /robot/spray  — publish MQTT spray command
# TODO (Akontoke): GET  /robot/status — return live sprayer + solar battery status

@router.post("/spray")
async def trigger_spray():
    return {"status": "command_sent"}

@router.get("/status")
async def robot_status():
    return {"spraying": False, "battery": 0, "solar": 0}
