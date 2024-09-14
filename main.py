import requests

# Function to send SMS
def send_sms(api_key, phone_number, message_content, brand_name, no_sms_flag):
    api_url = 'https://nando.ge/api.php'

    # Data to be sent in the POST request
    post_data = {
        'brand_name': brand_name,
        'apikey': api_key,
        'destination': phone_number,
        'content': message_content,
        'no_sms': no_sms_flag
    }

    try:
        # Make the POST request to send SMS
        response = requests.post(api_url, data=post_data)

        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

# Main code to send the message
api_key = 'c8214ac78ae915da714d50f02449aaf9e02904d4d4b7c3f10d63be97a652b32e'
brand_name = 'MatMartivad'
phone_number = "595018979"  # Ensure the phone number is a string
message_content = f'ტესტის ქულა: 8 / 10. რეკომენდაცია - გაიმეოროს პარაგრაფები: §2, §5, §12'
no_sms_flag = 'false'

# Assuming index is defined elsewhere, if not you can set it to 1 or remove this line
index = 1  # Example index value, replace it with your own logic

# Print the message content
print(f"text {index}: {message_content}")

# Send the SMS using the send_sms function
report = send_sms(api_key, phone_number, message_content, brand_name, no_sms_flag)
print(report)
