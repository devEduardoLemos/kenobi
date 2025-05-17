from dataclasses import dataclass

@dataclass
class ResponseDTO:
    """Data Transfer Object for FINEP Calls"""
    title: str 
    resume: str
    publication_date: str
    deadline: str
    funding_source: str
    target_audience: str
    theme: str
    link: str
    status: str
