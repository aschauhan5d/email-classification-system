import re
from typing import Tuple, List, Dict

def mask_pii(text: str) -> Tuple[str, List[Dict]]:
    """Mask PII in text and return masked text with entities found"""
    patterns = {
        'phone': r'(\+?\d{1,3}[- ]?)?\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}',
        'email': r'\S+@\S+\.\S+',
        'aadhar': r'\d{4}[ -]?\d{4}[ -]?\d{4}',
        'credit_card': r'\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}'
    }

    entities = []
    masked_text = text

    for pii_type, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            start, end = match.span()
            
            # Skip overlaps
            if any(e['position'][0] <= start < e['position'][1] for e in entities):
                continue
                
            entities.append({
                'position': [start, end],
                'classification': pii_type,
                'entity': match.group()
            })
            
            masked_text = masked_text[:start] + f'[{pii_type}]' + masked_text[end:]
    
    return masked_text, entities