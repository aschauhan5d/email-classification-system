from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models import predict_category
from utils import mask_pii

router = APIRouter()

class EmailRequest(BaseModel):
    email_body: str

class EntityResponse(BaseModel):
    position: list[int]
    classification: str
    entity: str

class EmailResponse(BaseModel):
    input_email_body: str
    list_of_masked_entities: list[EntityResponse]
    masked_email: str
    category_of_the_email: str

@router.post("/classify", response_model=EmailResponse)
def classify_email(request: EmailRequest):
    try:
        masked_text, entities = mask_pii(request.email_body)
        category = predict_category(request.email_body)
        
        return {
            "input_email_body": request.email_body,
            "list_of_masked_entities": entities,
            "masked_email": masked_text,
            "category_of_the_email": category
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))