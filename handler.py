import boto3
import json

client = boto3.client('cognito-idp')

def pre_token_auth_lambda(event, context):
    new_scopes = [item for item in event['request']['groupConfiguration']['groupsToOverride']]
    event['response'] = {
        "claimsOverrideDetails": {
            "claimsToAddOrOverride": {
                "scope": " ".join(new_scopes),
            }
        }
    }
    print(event)
    return event

def register_regular_user(event, context):
    pass

def lambda_for_admin_users(event, context):
    response = {
        'statusCode': 200,
        'body': json.dumps('Hello from Admin User')
    }
    return response

def lambda_for_regular_users(event, context):
    response = {
        'statusCode': 200,
        'body': json.dumps('Hello from Reegular User')
    }
    return response