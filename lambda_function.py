import json
import os
from _tasks.hello_world import greet_user
from datetime import datetime, UTC

def create_mcp_response(message, context=None, metadata=None):
    """
    Create MCP-compliant response.

    The MCP server provides two functions:
    1. `hello_world`: A function that takes no parameters and returns the string "Hello, World!".
    2. `greet_user`: A function that takes a single parameter (`username`) and returns a personalized greeting message.
    """
    return {
        'message': message,
        'context': context or {},
        'metadata': metadata or {
            'service': 'hello_world_mcp',
            'version': '1.0.0',
            'description': "This MCP server provides two functions: "
                           "1. `hello_world`: A function that takes no parameters and returns 'Hello, World!'. "
                           "2. `greet_user`: A function that takes a single parameter (`username`) and returns a personalized greeting.",
            'timestamp': str(datetime.now(UTC))
        }
    }

def lambda_handler(event, context):
    try:
        # Check if it's an MCP request
        is_mcp = event.get('requestContext', {}).get('http', {}).get('path', '').endswith('/mcp/process')
        
        if is_mcp and event.get('requestContext', {}).get('http', {}).get('method') == 'POST':
            # Handle MCP request
            body = json.loads(event.get('body', '{}'))
            username = body.get('username')
            user_context = body.get('context', {})
            user_metadata = body.get('metadata', {})
            
            if username is None:
                return {
                    'statusCode': 400,
                    'headers': {'Access-Control-Allow-Origin': '*'},
                    'body': json.dumps(create_mcp_response("Username parameter is required"))
                }
            
            result = greet_user(username)
            return {
                'statusCode': 200,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps(create_mcp_response(result, user_context, user_metadata))
            }
        
        # Handle regular request
        username = event.get('queryStringParameters', {}).get('username')
        
        if username is None:
            return {
                'statusCode': 400,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps("Username parameter is required")
            }

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(greet_user(username))
        }

    except Exception as err:
        error_response = create_mcp_response(f"Internal server error: {str(err)}") if is_mcp else f"Internal server error: {str(err)}"
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(error_response)
        } 