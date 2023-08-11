import uvicorn

if __name__ == "__main__":
    uvicorn.run("todo-app.app:app", reload=True)
