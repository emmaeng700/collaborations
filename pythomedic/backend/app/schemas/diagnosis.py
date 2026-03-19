from pydantic import BaseModel

# TODO (Oppong): Finalize disease label list from your 3,243-image dataset

class DiagnosisResponse(BaseModel):
    disease: str
    confidence: float
    advice: str
