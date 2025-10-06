from ninja import Schema

class BarkSchemaOut(Schema):
    """Schema for bark responses"""
    id: int
    message: str

class ErrorSchemaOut(Schema):
    error: str