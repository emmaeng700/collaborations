from fastapi import FastAPI

app = FastAPI(
    title="Pythomedic API",
    description="Plant disease diagnosis + robot sprayer control",
    version="1.0.0"
)

# TODO (Akontoke): Register routers below once each is built
# from app.routers import diagnose, robot, history
# app.include_router(diagnose.router)
# app.include_router(robot.router)
# app.include_router(history.router)

@app.get("/")
def root():
    return {"status": "Pythomedic API running"}
