from fastapi import FastAPI, Request, Response
from proxy_server import handle_request

app = FastAPI()

origin_server: str | None = None


@app.api_route("/{path:path}", methods=["GET"])
async def proxy(request: Request, path: str):

    if origin_server is None:
        return Response("Origin server not configured", status_code=500)    

    result, cache_status = await handle_request(request, origin_server) # pyright: ignore[reportGeneralTypeIssues]

    headers = result["headers"]
    headers["X-Cache"] = cache_status

    return Response(
        content=result["content"],
        status_code=result["status"],
        headers=headers
    )