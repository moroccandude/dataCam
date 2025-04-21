from  fastapi import FastAPI

app=FastAPI()

@app.get("/getdata")
def read_root():
   return {"status": "secuss"}

