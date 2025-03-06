# import streamlit as st
# import pandas as pd
# from twilio.rest import Client
# import random

# # Twilio Credentials
# TWILIO_SID = "ACa69ccec0ce83d59b0ebad27f15e63481"
# TWILIO_AUTH_TOKEN = "92b96d5c931a745fe6ec367d62e7d204"
# TWILIO_PHONE = "SWIFTPLAY"

# # Initialize Twilio Client
# # client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# # OTP Sending Function
# def send_otp(phone_number):
#     otp = random.randint(100000, 999999)  # Generate Random OTP
#     message = f"Your OTP is {otp}. Please do not share it with anyone."
    
#     try:
#         sms = client.messages.create(
#             body=message,
#             from_=TWILIO_PHONE,
#             to=phone_number
#         )
#         return f"📲 OTP sent to {phone_number} | SID: {sms.sid}"
#     except Exception as e:
#         return f"❌ Error sending OTP to {phone_number}: {str(e)}"

# # Streamlit UI
# st.title("📩 SWIFTSTAY OTP Sender")

# # Country Code Selection with Country Name
# countries = {
#      "Afghanistan (+93)": "+93",
#     "Albania (+355)": "+355",
#     "Algeria (+213)": "+213",
#     "Andorra (+376)": "+376",
#     "Angola (+244)": "+244",
#     "Antigua and Barbuda (+1-268)": "+1-268",
#     "Argentina (+54)": "+54",
#     "Armenia (+374)": "+374",
#     "Australia (+61)": "+61",
#     "Austria (+43)": "+43",
#     "Azerbaijan (+994)": "+994",
#     "Bahamas (+1-242)": "+1-242",
#     "Bahrain (+973)": "+973",
#     "Bangladesh (+880)": "+880",
#     "Barbados (+1-246)": "+1-246",
#     "Belarus (+375)": "+375",
#     "Belgium (+32)": "+32",
#     "Belize (+501)": "+501",
#     "Benin (+229)": "+229",
#     "Bhutan (+975)": "+975",
#     "Bolivia (+591)": "+591",
#     "Bosnia and Herzegovina (+387)": "+387",
#     "Botswana (+267)": "+267",
#     "Brazil (+55)": "+55",
#     "Brunei (+673)": "+673",
#     "Bulgaria (+359)": "+359",
#     "Burkina Faso (+226)": "+226",
#     "Burundi (+257)": "+257",
#     "Cabo Verde (+238)": "+238",
#     "Cambodia (+855)": "+855",
#     "Cameroon (+237)": "+237",
#     "Canada (+1)": "+1",
#     "Central African Republic (+236)": "+236",
#     "Chad (+235)": "+235",
#     "Chile (+56)": "+56",
#     "China (+86)": "+86",
#     "Colombia (+57)": "+57",
#     "Comoros (+269)": "+269",
#     "Congo (Congo-Brazzaville) (+242)": "+242",
#     "Costa Rica (+506)": "+506",
#     "Croatia (+385)": "+385",
#     "Cuba (+53)": "+53",
#     "Cyprus (+357)": "+357",
#     "Czechia (+420)": "+420",
#     "Democratic Republic of the Congo (+243)": "+243",
#     "Denmark (+45)": "+45",
#     "Djibouti (+253)": "+253",
#     "Dominica (+1-767)": "+1-767",
#     "Dominican Republic (+1-809)": "+1-809",
#     "Ecuador (+593)": "+593",
#     "Egypt (+20)": "+20",
#     "El Salvador (+503)": "+503",
#     "Equatorial Guinea (+240)": "+240",
#     "Eritrea (+291)": "+291",
#     "Estonia (+372)": "+372",
#     "Eswatini (+268)": "+268",
#     "Ethiopia (+251)": "+251",
#     "Fiji (+679)": "+679",
#     "Finland (+358)": "+358",
#     "France (+33)": "+33",
#     "Gabon (+241)": "+241",
#     "Gambia (+220)": "+220",
#     "Georgia (+995)": "+995",
#     "Germany (+49)": "+49",
#     "Ghana (+233)": "+233",
#     "Greece (+30)": "+30",
#     "Grenada (+1-473)": "+1-473",
#     "Guatemala (+502)": "+502",
#     "Guinea (+224)": "+224",
#     "Guinea-Bissau (+245)": "+245",
#     "Guyana (+592)": "+592",
#     "Haiti (+509)": "+509",
#     "Honduras (+504)": "+504",
#     "Hungary (+36)": "+36",
#     "Iceland (+354)": "+354",
#     "India (+91)": "+91",
#     "Indonesia (+62)": "+62",
#     "Iran (+98)": "+98",
#     "Iraq (+964)": "+964",
#     "Ireland (+353)": "+353",
#     "Israel (+972)": "+972",
#     "Italy (+39)": "+39",
#     "Jamaica (+1-876)": "+1-876",
#     "Japan (+81)": "+81",
#     "Jordan (+962)": "+962",
#     "Kazakhstan (+7)": "+7",
#     "Kenya (+254)": "+254",
#     "Kiribati (+686)": "+686",
#     "Kuwait (+965)": "+965",
#     "Kyrgyzstan (+996)": "+996",
#     "Laos (+856)": "+856",
#     "Latvia (+371)": "+371",
#     "Lebanon (+961)": "+961",
#     "Lesotho (+266)": "+266",
#     "Liberia (+231)": "+231",
#     "Libya (+218)": "+218",
#     "Liechtenstein (+423)": "+423",
#     "Lithuania (+370)": "+370",
#     "Luxembourg (+352)": "+352",
#     "Madagascar (+261)": "+261",
#     "Malawi (+265)": "+265",
#     "Malaysia (+60)": "+60",
#     "Maldives (+960)": "+960",
#     "Mali (+223)": "+223",
#     "Malta (+356)": "+356",
#     "Marshall Islands (+692)": "+692",
#     "Mauritania (+222)": "+222",
#     "Mauritius (+230)": "+230",
#     "Mexico (+52)": "+52",
#     "Micronesia (+691)": "+691",
#     "Moldova (+373)": "+373",
#     "Monaco (+377)": "+377",
#     "Mongolia (+976)": "+976",
#     "Zimbabwe (+263)": "+263",

# }

# # Combined Input for Country Code and Phone Number
# col1, col2 = st.columns([2, 3])
# with col1:
#     country_name = st.selectbox("🌍 Select Country", list(countries.keys()))
#     country_code = countries[country_name]
# with col2:
#     phone_number = st.text_input("📞 Enter Phone Number", placeholder="1234567890")

# # Button to Send OTP
# if st.button("🚀 Send OTP"):
#     if phone_number:
#         full_number = country_code + phone_number
#         with st.spinner("Sending OTP... Please wait"):
#             response = send_otp(full_number)
#         st.write(response)
#     else:
#         st.error("❌ Please enter a valid phone number!")







import streamlit as st
import random

# OTP Sending Function (Fake)
def send_otp(phone_number):
    return "Twilio OTP: You can perform illegal activity, you are blocked. OTP not sent."

# Streamlit UI
st.title("📩 SWIFTSTAY OTP Sender")

# Country Code Selection with Country Name
countries = {
      "Afghanistan (+93)": "+93",
    "Albania (+355)": "+355",
    "Algeria (+213)": "+213",
    "Andorra (+376)": "+376",
    "Angola (+244)": "+244",
    "Antigua and Barbuda (+1-268)": "+1-268",
    "Argentina (+54)": "+54",
    "Armenia (+374)": "+374",
    "Australia (+61)": "+61",
    "Austria (+43)": "+43",
    "Azerbaijan (+994)": "+994",
    "Bahamas (+1-242)": "+1-242",
    "Bahrain (+973)": "+973",
    "Bangladesh (+880)": "+880",
    "Barbados (+1-246)": "+1-246",
    "Belarus (+375)": "+375",
    "Belgium (+32)": "+32",
    "Belize (+501)": "+501",
    "Benin (+229)": "+229",
    "Bhutan (+975)": "+975",
    "Bolivia (+591)": "+591",
    "Bosnia and Herzegovina (+387)": "+387",
    "Botswana (+267)": "+267",
    "Brazil (+55)": "+55",
    "Brunei (+673)": "+673",
    "Bulgaria (+359)": "+359",
    "Burkina Faso (+226)": "+226",
    "Burundi (+257)": "+257",
    "Cabo Verde (+238)": "+238",
    "Cambodia (+855)": "+855",
    "Cameroon (+237)": "+237",
    "Canada (+1)": "+1",
    "Central African Republic (+236)": "+236",
    "Chad (+235)": "+235",
    "Chile (+56)": "+56",
    "China (+86)": "+86",
    "Colombia (+57)": "+57",
    "Comoros (+269)": "+269",
    "Congo (Congo-Brazzaville) (+242)": "+242",
    "Costa Rica (+506)": "+506",
    "Croatia (+385)": "+385",
    "Cuba (+53)": "+53",
    "Cyprus (+357)": "+357",
    "Czechia (+420)": "+420",
    "Democratic Republic of the Congo (+243)": "+243",
    "Denmark (+45)": "+45",
    "Djibouti (+253)": "+253",
    "Dominica (+1-767)": "+1-767",
    "Dominican Republic (+1-809)": "+1-809",
    "Ecuador (+593)": "+593",
    "Egypt (+20)": "+20",
    "El Salvador (+503)": "+503",
    "Equatorial Guinea (+240)": "+240",
    "Eritrea (+291)": "+291",
    "Estonia (+372)": "+372",
    "Eswatini (+268)": "+268",
    "Ethiopia (+251)": "+251",
    "Fiji (+679)": "+679",
    "Finland (+358)": "+358",
    "France (+33)": "+33",
    "Gabon (+241)": "+241",
    "Gambia (+220)": "+220",
    "Georgia (+995)": "+995",
    "Germany (+49)": "+49",
    "Ghana (+233)": "+233",
    "Greece (+30)": "+30",
    "Grenada (+1-473)": "+1-473",
    "Guatemala (+502)": "+502",
    "Guinea (+224)": "+224",
    "Guinea-Bissau (+245)": "+245",
    "Guyana (+592)": "+592",
    "Haiti (+509)": "+509",
    "Honduras (+504)": "+504",
    "Hungary (+36)": "+36",
    "Iceland (+354)": "+354",
    "India (+91)": "+91",
    "Indonesia (+62)": "+62",
    "Iran (+98)": "+98",
    "Iraq (+964)": "+964",
    "Ireland (+353)": "+353",
    "Israel (+972)": "+972",
    "Italy (+39)": "+39",
    "Jamaica (+1-876)": "+1-876",
    "Japan (+81)": "+81",
    "Jordan (+962)": "+962",
    "Kazakhstan (+7)": "+7",
    "Kenya (+254)": "+254",
    "Kiribati (+686)": "+686",
    "Kuwait (+965)": "+965",
    "Kyrgyzstan (+996)": "+996",
    "Laos (+856)": "+856",
    "Latvia (+371)": "+371",
    "Lebanon (+961)": "+961",
    "Lesotho (+266)": "+266",
    "Liberia (+231)": "+231",
    "Libya (+218)": "+218",
    "Liechtenstein (+423)": "+423",
    "Lithuania (+370)": "+370",
    "Luxembourg (+352)": "+352",
    "Madagascar (+261)": "+261",
    "Malawi (+265)": "+265",
    "Malaysia (+60)": "+60",
    "Maldives (+960)": "+960",
    "Mali (+223)": "+223",
    "Malta (+356)": "+356",
    "Marshall Islands (+692)": "+692",
    "Mauritania (+222)": "+222",
    "Mauritius (+230)": "+230",
    "Mexico (+52)": "+52",
    "Micronesia (+691)": "+691",
    "Moldova (+373)": "+373",
    "Monaco (+377)": "+377",
    "Mongolia (+976)": "+976",
    "Zimbabwe (+263)": "+263",
}

# Combined Input for Country Code and Phone Number
col1, col2 = st.columns([2, 3])
with col1:
    country_name = st.selectbox("🌍 Select Country", list(countries.keys()))
    country_code = countries[country_name]
with col2:
    phone_number = st.text_input("📞 Enter Phone Number", placeholder="1234567890")

# Button to Send OTP
if st.button("🚀 Send OTP"):
    if phone_number:
        full_number = country_code + phone_number
        with st.spinner("Sending OTP... Please wait"):
            response = send_otp(full_number)
        st.write(response)
    else:
        st.error("❌ Please enter a valid phone number!")

