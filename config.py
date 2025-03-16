import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # API Configuration
    API_VERSION = "1.0.0"
    API_PREFIX = "/api/v1"
    
    # AWS Configuration
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    
    # MCP Configuration
    MCP_VERSION = "1.0.0"
    MCP_ENDPOINTS = {
        "process": "/mcp/process",
        "health": "/health"
    }
    
    # AI Integration Settings
    CURSOR_AI_KEY = os.getenv("CURSOR_AI_KEY", "")
    WINDSURF_MCP_KEY = os.getenv("WINDSURF_MCP_KEY", "")
    
    @staticmethod
    def get_mcp_metadata() -> Dict[str, Any]:
        return {
            "service": "hello_world_mcp",
            "version": Config.API_VERSION,
            "mcp_version": Config.MCP_VERSION,
            "supported_features": ["basic_greeting", "context_aware"]
        }

config = Config() 