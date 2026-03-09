import httpx
from cache import get_cache, set_cache


async def handle_request(request, origin):

    # cache_key = f"{request.method}:{request.url.path}?{request.url.query}"
    cache_key = f"{request.method}:{str(request.url)}"

    cached = get_cache(cache_key)

    if cached:
        return cached, "HIT"

    try:

        headers = dict(request.headers)
        headers.pop("host", None)
        

        origin_url = origin + request.url.path

        if request.url.query:
            origin_url += f"?{request.url.query}"

        async with httpx.AsyncClient() as client:

            response = await client.request(
                method=request.method,
                url=origin_url,
                headers=headers,
                content=await request.body()
            )

    except Exception as e:

        return {
            "status": 502,
            "headers": {},
            "content": f"Proxy error: {str(e)}".encode()
        }, "MISS"

    result = {
        "status": response.status_code,
        "headers": dict(response.headers),
        "content": response.content
    }

    if request.method == "GET":
        set_cache(cache_key, result)

    else:
        return result, "MISS"