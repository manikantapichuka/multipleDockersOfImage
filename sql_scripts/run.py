# import os
# import uvicorn
# from dotenv import load_dotenv

# load_dotenv()

# host_ip="0.0.0.0"
# host_port=8003

# def run():
#     """Function to run FastAPI with Uvicorn using uvicorn.run()"""
#     uvicorn.run("main:app", host=host_ip, port=host_port, reload=True)

# if __name__ == "__main__":
#     run()
    
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8003, reload=False)
