from CollectionService import payment_create
from dataclasses import asdict

def create(bill_data, RequestInfo):
    # Create PaymentDetail object
    payment_detail = payment_create.PaymentDetail(
        businessService=bill_data["businessService"],
        billId=bill_data["id"],
        totalDue=bill_data["totalAmount"],
        totalAmountPaid=bill_data["totalAmount"]
    )

    # Create Payment object
    payment = payment_create.Payment(
        mobileNumber=bill_data["mobileNumber"],
        paymentDetails=[payment_detail],
        tenantId=bill_data["tenantId"],
        totalDue=bill_data["totalAmount"],
        totalAmountPaid=bill_data["totalAmount"],
        paymentMode="CASH",
        payerName=bill_data["payerName"],
        paidBy="OWNER"
    )

    # Create the final payload
    payment_payload = payment_create.RequestPayload(
        Payment=payment,
        RequestInfo=RequestInfo
    )

    return asdict(payment_payload)