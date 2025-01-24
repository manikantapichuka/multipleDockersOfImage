# import os
# import sys

# # Add pyarmor_runtime_000000 directory to sys.path to make runtime available
# runtime_path = os.path.join(os.path.dirname(__file__), "pyarmor_runtime_000000")
# if runtime_path not in sys.path:
#     sys.path.append(runtime_path)

# # Initialize the PyArmor runtime
# try:
#     from pyarmor_runtime import pyarmor_runtime
#     pyarmor_runtime()  # Initialize the PyArmor runtime
# except ModuleNotFoundError as e:
#     print(f"Error: {e}")
#     print("PyArmor runtime module not found. Check if pyarmor_runtime_000000 is correctly included.")
#     sys.exit(1)

# # Import FastAPI app from main.py
# from main import app

# # Run the FastAPI server if necessary (for debugging only)
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("APP_PORT", 8004)))

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=False)
