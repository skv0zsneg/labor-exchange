# labor-exchange
FAST API labor exchange project. Made for study propose.

## Made by lessons from Youtube:
- https://www.youtube.com/watch?v=PVebRy0_K0s&ab_channel=DevRoadX
- https://www.youtube.com/watch?v=qduT62Bygyw&ab_channel=DevRoadX


## Used:
- Python 3.9
- FastAPI
- Uvicorn

## Launch
```
~ pip3 install -r requirements.txt
~ sudo docker-compose -f docker-compose.dev.yaml up
~ export EE_DATABASE_URL="postgresql://root:root@localhost:32700/employment_exchange"
~ python3 main.py
```