from typing import Literal
from pydantic import BaseModel

class StudentInput(BaseModel):
    school: Literal["GP", "MS"]
    sex: Literal["F", "M"]
    age: int
    address: Literal["U", "R"]
    famsize: Literal["LE3", "GT3"]
    Pstatus: Literal["T", "A"]
    Medu: int
    Fedu: int
    Mjob: str
    Fjob: str
    reason: str
    guardian: str
    traveltime: int
    studytime: int
    failures: int
    schoolsup: Literal["yes", "no"]
    famsup: Literal["yes", "no"]
    paid: Literal["yes", "no"]
    activities: Literal["yes", "no"]
    nursery: Literal["yes", "no"]
    higher: Literal["yes", "no"]
    internet: Literal["yes", "no"]
    romantic: Literal["yes", "no"]
    famrel: int
    freetime: int
    goout: int
    Dalc: int
    Walc: int
    health: int
    absences: int
    G1: int
    G2: int
    subject: Literal["mat", "por"]