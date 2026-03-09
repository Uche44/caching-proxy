import argparse
import uvicorn
import main
from cache import clear_cache

def start_server(port, origin):

    main.origin_server = origin

    uvicorn.run(
        "main:app",
        host = "0.0.0.0",
        port = port,
        reload = False
    )

def main_cli():

    parser = argparse.ArgumentParser()

    parser.add_argument("--port", type=int, help="Port to run proxy server")
    parser.add_argument("--origin", type=str, help="Origin server URL")
    parser.add_argument("--clear-cache", action="store_true")

    args = parser.parse_args()

    if args.clear_cache:
        clear_cache()    
        print("Cache cleared")
        return
    
    if args.port and args.origin:
        start_server(args.port, args.origin)
    else:
        print("Usage:")
        print("python cli.py --port 3000 --origin https://jsonplaceholder.typicode.com")    

if __name__ == "__main__":
    main_cli()        