from dataclasses import dataclass

@dataclass
class ResponseDTO:
    """Data Transfer Object for FINEP Calls"""
    title: str 
    resume: str
    publicationDate: str
    deadline: str
    fundingSource: str
    targetAudience: str
    theme: str
    link: str
    status: str
