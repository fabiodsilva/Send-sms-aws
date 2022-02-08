#!/usr/env/python
import boto3
import sys
from botocore.exceptions import ClientError


# The AWS Region that you want to use to send the message. For a list of
# AWS Regions where the Amazon Pinpoint API is available, see
# https://docs.aws.amazon.com/pinpoint/latest/apireference/
region = "us-east-1"

# The phone number or short code to send the message from. The phone number
# or short code that you specify has to be associated with your Amazon Pinpoint
# account. For best results, specify long codes in E.164 format.
originationNumber = ""



# The recipient's phone number.  For best results, you should specify the

destinationNumber = sys.argv[1]

# The content of the SMS message.
message = sys.argv[2]

# The Amazon Pinpoint project/application ID to use when you send this message.
# Make sure that the SMS channel is enabled for the project or application
# that you choose.
applicationId = "5be7944ca51245cd909267f4ceed7ee1"

# The type of SMS message that you want to send. If you plan to send
# time-sensitive content, specify TRANSACTIONAL. If you plan to send
# marketing-related content, specify PROMOTIONAL.
messageType = "PROMOTIONAL"

# The registered keyword associated with the originating short code.
registeredKeyword = ""

# The sender ID to use when sending the message. Support for sender ID
# varies by country or region. For more information, see
# https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html
senderId = ""

# Create a new client and specify a region.
client = boto3.client('pinpoint',region_name=region)
try:
    response = client.send_messages(
        ApplicationId=applicationId,
        MessageRequest={
            'Addresses': {
                destinationNumber: {
                    'ChannelType': 'SMS'
                }
            },
            'MessageConfiguration': {
                'SMSMessage': {
                    'Body': message,
                    'Keyword': registeredKeyword,
                    'MessageType': messageType,
                    'OriginationNumber': originationNumber,
                    'SenderId': senderId
                }
            }
        }
    )

except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Message sent! Message ID: "
            + response['MessageResponse']['Result'][destinationNumber]['MessageId'])