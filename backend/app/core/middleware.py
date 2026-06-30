from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import time

from app.core.logging import logger

class LoggingMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(
        self,
        request: Request,
        call_next
    ) -> Response:
        
        start_time = time.time()
        
        response = await call_next(request)
        
        process_time = time.time() - start_time
        
        
        logger.info(
            f"{request.method} | {request.url.path} - "
            f"Status: {response.status_code} - "
            f"Duration: {process_time*1000:.3f}s"
        )
        
        return response