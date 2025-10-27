from fastapi import FastAPI

# 创建 FastAPI 实例
app = FastAPI(title="简单API服务", version="1.0.0")

# 根路径
@app.get("/")
async def root():
    return {"message": "欢迎使用 FastAPI 服务！"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


