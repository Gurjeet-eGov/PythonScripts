from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class PaymentDetail:
    businessService: str
    billId: str
    totalDue: float
    totalAmountPaid: float

@dataclass
class Payment:
    mobileNumber: str
    paymentDetails: List[PaymentDetail]
    tenantId: str
    totalDue: float
    totalAmountPaid: float
    paymentMode: str
    payerName: str
    paidBy: str

@dataclass
class RequestPayload:
    Payment: Payment
    RequestInfo: dict = field(default_factory=dict)
