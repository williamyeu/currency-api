# currency-api

## 運行api

1. 安裝python https://www.python.org/
2. 建立虛擬環境
```
python3 -m venv .venv
```
3. activate 虛擬環境
```
source .venv/bin/activate
```
4. 安裝packages
```
pip install -r requirements.txt
```

5. 啟動fastapi
```
uvicorn main:app
```

6. api會運行在localhost:8000

## 運行測試
```
pytest test_main.py
```
