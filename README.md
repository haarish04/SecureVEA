# VEA - Vulnerable & Emergency Authentication

## Go to /docs for setup of project

## What is VEA?

VEA is a special authentication process used when a customer cannot authenticate using preferred methods and is in a vulnerable or emergency situation.

## When Does VEA Apply?

Examples of scenarios where VEA is applied include:

- Domestic and family violence (Safe)
- Aboriginal or Torres Strait Islander (First Nations)
- Life-threatening medical condition (Priority Assistance)
- Bereavement (Compassionate Care)
- Safety at risk
- Elderly or digitally excluded
- Physical injury, illness, or disability
- Living rurally or remotely
- Affected by natural disaster
- No valid ID due to emergency

## Key Process Points

- Make all reasonable attempts to authenticate using standard methods first (e.g., in-app challenge, OTC/OTP, outbound call, DVS).
- If those fail and vulnerability/emergency is confirmed, call the dedicated VEA Team via IVR to progress further.
- Certain cases (e.g., Domestic & Family Violence, Priority Assistance) have specialist teams trained to handle them.

## How the Application Helps

The application provides sufficient proof to agents to decide if the case is a legitimate VEA scenario or not by utilizing key fraud and risk signals from network APIs and device checks.

## Network APIs Used

- **Call Forwarding Signal:** Detects if call forwarding is set up on the device, indicative of potential verification calls being redirected to attackers. Returns `true` if call forwarding is enabled.
- **Device Swap:** Detects if the device has been swapped for a particular SIM card. Returns `true` if a device swap is detected.
- **Number Recycling:** Detects if the phone number has been recycled to a new user.
- **Scam Signal:** (Currently not available in Camara)
- **Sim Swap:** Detects if the SIM has been swapped (a new SIM card activated for an existing number). Returns the timestamp of the SIM swap action.
- **Device Identifier:** Retrieves IMEI and manufacturer/model information of the device.
- **Device Reachability Status:** Detects if a mobile device is reachable on the network and any change in its status.
- **Location Retrieval:** Detects unusual locations for the customer device.

---

This README serves as documentation for the VEA authentication solution, outlining key concepts, process steps, and the network APIs leveraged to make fraud risk assessments.
