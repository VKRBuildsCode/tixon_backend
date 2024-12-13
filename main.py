import requests as rq
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import random
from supabase import create_client, Client
supabase: Client = create_client("https://ekzrxzccleshjwocdwrk.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVrenJ4emNjbGVzaGp3b2Nkd3JrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzQwNzYwOTEsImV4cCI6MjA0OTY1MjA5MX0.RWsM2pTodkyr9QgNni7QJ6eDnNmbK1Y45vm0RGEDT5s")
response = supabase.storage.from_(id="tixon").list("folder")
print(response)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)
access_token="1000.6a3143214393e5174a1cdb76829fcf0a.e40c23e20dced0b0056869a51f407184"
result_events=rq.request(url="https://zohoapis.in/backstage/v3/portals/60034551768/events",method="get",headers={
    "Authorization":"Zoho-oauthtoken "+access_token})
if(result_events.json()=={"status_code":"401","message":"Please provide a valid OAuthScope"}):
    result=rq.request(url="https://accounts.zoho.in/oauth/v2/token?client_id=1000.G5JKYIDEPYVOJG1I2P618NTBEZXKVV&client_secret=bf458d3bd3d88a0687d91b242f8043ca12c5da0504&grant_type=refresh_token&code=1000.c3da05e7d19d9cc7b8f5fcd9cc6ba1c0.9a834b3f4d9be4ffaae3a97b53d01f09&scope=zohobackstage.event.READ&refresh_token=1000.3dc4a084c322c71f37678a87c9e8858b.99472d094d3ade6926370e12d1c8f65f",method="post")
    access_token=result.json()['access_token']
    result_events=rq.request(url="https://zohoapis.in/backstage/v3/portals/60034551768/events",method="get",headers={
        "Authorization":"Zoho-oauthtoken "+access_token})
print(result_events.json()['events'][0])
@app.get("/events")
def get_events():
    global  access_token
    result_events=rq.request(url="https://zohoapis.in/backstage/v3/portals/60034551768/events",method="get",headers={
            "Authorization":"Zoho-oauthtoken "+access_token
        })
    if(result_events.json()=={"status_code":"401","message":"Please provide a valid OAuthScope"}):
        result=rq.request(url="https://accounts.zoho.in/oauth/v2/token?client_id=1000.G5JKYIDEPYVOJG1I2P618NTBEZXKVV&client_secret=bf458d3bd3d88a0687d91b242f8043ca12c5da0504&grant_type=refresh_token&code=1000.c3da05e7d19d9cc7b8f5fcd9cc6ba1c0.9a834b3f4d9be4ffaae3a97b53d01f09&scope=zohobackstage.event.READ&refresh_token=1000.3dc4a084c322c71f37678a87c9e8858b.99472d094d3ade6926370e12d1c8f65f",method="post")
        access_token=result.json()['access_token']
        result_events=rq.request(url="https://zohoapis.in/backstage/v3/portals/60034551768/events",method="get",headers={
    "Authorization":"Zoho-oauthtoken "+access_token})
        events=result_events.json()['events']
        random.shuffle(events)
        return events
    events=result_events.json()['events']
    random.shuffle(events)
    return events
@app.get("/events_names")
def get_events_names():
    events_names=[]
    global  access_token
    result_events=rq.request(url="https://zohoapis.in/backstage/v3/portals/60034551768/events",method="get",headers={
    "Authorization":"Zoho-oauthtoken "+access_token})
    for i in range(0,result_events.json()['events']):
        pass
    return result_events.json()['events']

