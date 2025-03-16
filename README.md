# Hello World MCP Server

A simple Hello World service with Model Context Protocol (MCP) support for Cursor AI integration.

## Features

- Simple GET endpoint for basic hello world functionality
- MCP-compliant endpoint for Cursor AI integration
- AWS Lambda deployment ready
- Context-aware processing
- Error handling

## Setup Instructions

1. **AWS Lambda Setup**
   ```bash
   # Package the application
   zip -r deployment.zip lambda_function.py _tasks/
   ```
   - Upload to AWS Lambda
   - Set the handler to `lambda_function.lambda_handler`
   - Set Python runtime to 3.9 or later

2. **API Gateway Configuration**
   - Create two routes in API Gateway:
     1. GET /?username={username} (legacy endpoint)
     2. POST /mcp/process (MCP endpoint)
   - Integrate both routes with your Lambda function
   - Enable CORS for both routes
   - Deploy your API

## Using the API

### 1. Basic Usage (Legacy Endpoint)
```bash
curl -X GET "https://your-api-url/?username=John"
```
Response:
```json
"Hello World, John!"
```

### 2. MCP Endpoint for Cursor Integration
```bash
curl -X POST "https://your-api-url/mcp/process" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "John",
       "context": {},
       "metadata": {}
     }'
```
Response:
```json
{
    "message": "Hello World, John!",
    "context": {},
    "metadata": {
        "service": "hello_world_mcp",
        "version": "1.0.0",
        "timestamp": "2024-03-15T12:00:00Z"
    }
}
```

## Integrating with Cursor AI

1. **Install Cursor**
   - Download and install Cursor from https://cursor.sh
   - Open Cursor and sign in

2. **Configure MCP Integration**
   - Open Cursor Settings
   - Navigate to AI > Model Context Protocol
   - Click "Add New MCP Endpoint"
   - Configure your endpoint:
     ```
     Name: Hello World MCP
     URL: https://your-api-url/mcp/process
     Method: POST
     Headers: 
       Content-Type: application/json
     ```

3. **Test the Integration**
   - In Cursor, open the Command Palette (Cmd/Ctrl + Shift + P)
   - Type "Hello World MCP"
   - Enter a username when prompted
   - The response will include:
     - The greeting message
     - Context information
     - Service metadata

4. **Using Context in Cursor**
   - The MCP endpoint maintains context between requests
   - You can send additional context in the request:
     ```json
     {
       "username": "John",
       "context": {
         "previous_greetings": ["Hello", "Hi"],
         "user_preferences": {"language": "en"}
       },
       "metadata": {
         "client": "cursor-ai",
         "version": "1.0.0"
       }
     }
     ```

## Error Handling

The API handles various error cases:
- Missing username: 400 Bad Request
- Server errors: 500 Internal Server Error
- All errors return MCP-compliant responses when using the MCP endpoint

## Security

- CORS enabled for cross-origin requests
- AWS IAM roles and policies should be configured
- API Gateway throttling recommended
- Consider adding API key requirement for production use

## Monitoring

- Use AWS CloudWatch for logs and metrics
- Monitor Lambda execution times and errors
- Set up CloudWatch alarms for error rates

## Troubleshooting

1. **CORS Issues**
   - Verify CORS headers in API Gateway
   - Check browser console for CORS errors
   - Ensure OPTIONS method is enabled

2. **Lambda Errors**
   - Check CloudWatch logs
   - Verify Lambda execution role
   - Test locally using AWS SAM

3. **Cursor Integration Issues**
   - Verify endpoint URL is correct
   - Check network connectivity
   - Ensure request format matches MCP specification