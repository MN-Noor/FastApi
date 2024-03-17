from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hi")
def greet():
    return "Hello? World?"

if __name__ == "__main__":
    uvicorn.run("hello:app", reload=True)
