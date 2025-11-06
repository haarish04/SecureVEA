from fastapi.middleware.cors import CORSMiddleware

def get_cors_config():
    return{
        "allow_origins": ["http://localhost:5173"],  # update with your frontend URL(s)
        "allow_credentials":True,
        "allow_methods": ["*"],
        "allow_headers": ["*"],
    }
