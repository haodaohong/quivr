from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    "https://laiwen.cn",
    "http://www.laiwen.cn",
    "https://quivr.laiwen.cn",
    "https://dev.laiwen.cn",
    "*",
]


def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
