from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/diagnose", tags=["Diagnosis"])

# TODO (Oppong): POST /diagnose
# - Accept image upload
# - Run classifier.py (OpenCV + model)
# - Return { disease, confidence, advice }

@router.post("/")
async def diagnose_plant(image: UploadFile = File(...)):
    # placeholder
    return {"disease": "", "confidence": 0.0, "advice": ""}
