from secure_passport_ext import CallerContext, A2AMessage, add_secure_passport, get_secure_passport

# 1. THE SENDER: Attaches the "Sidecar"
# We create a secure context with custom enterprise data
passport = CallerContext(
    client_id="a2a://travel-orchestrator.com",
    state={"tier": "Platinum", "billing_code": "US-123"},
    signature="valid-crypto-signature-123"
)

message = A2AMessage(type="task", content="Book flight")
# "Stamp" the message with the extension
add_secure_passport(message, passport)


# 2. THE RECEIVER: Inspects the "Sidecar"
# This function safely checks for the extension without crashing if missing
received_passport = get_secure_passport(message)

if received_passport and received_passport.is_verified:
    print(f"✅ Verified Platinum Request from: {received_passport.client_id}")
else: # Non-breaking fall-back behavior
    print(f"ℹ️ Standard processing (No auth extension found)")