from fastapi import APIRouter
from models import Complaint
from complaints import get_location
from fastapi.templating import Jinja2Templates
from fastapi import Request
from logger import logger
from email_notifier import send_email_notification



#here we are creating routes which means a chunk of your code is made, later on all are taken into a single file in main.py
router = APIRouter()
#fake_db = {}
fake_db = {
    1: Complaint(id=1, title="Water leakage", description="Raise in the bill without consumpsion" ,tatus="open", location="Bangalore"),
    2: Complaint(id=2, title="Electricity issue", description="Power outage for more than a day" , status="closed", location="Mumbai")
}

#we use here @routes bcoz it isn't the main file its the routes to which the main file will be given power to use
#we here make the complaints like creare them and take in the format defined in models.py
@router.post("/complaints")
def create_complaint(complaint: Complaint):
    fake_db[complaint.id] = complaint
    return {"message": "Complaint created", "data": complaint}


#here we read the complaints by listing them all from the values of the fakeDB database
@router.get("/complaints")
def get_complaints():
    return list(fake_db.values())


#we get to read teh complaints here with the help of the id specified
@router.get("/complaints/{id}")
def get_complaint(id: int):
    return fake_db.get(id)


#we update the complaints here by specifing the id and we get to update the complaint in the format we hv created in models.py
@router.put("/complaints/{id}")
def update_complaint(id: int, complaint: Complaint):
    if id in fake_db:
        fake_db[id] = complaint
        return {"message": "Complaint updated"}
    return {"error": "Not found"}


#this is mainly getting the location and adding it and using a api request to get the loc in the field
@router.post("/complaints/loc")
def create_complaint_loc(complaint: Complaint):
    complaint.location = get_location()
    fake_db[complaint.id] = complaint
    return {"message": "Complaint created", "data": complaint}


#it tells that we have a template for dashboard that should be used
templates = Jinja2Templates(directory="templates")
@router.get("/dashboard")
def dashboard(request: Request):
    complaints = list(fake_db.values())  # get all complaints
    return templates.TemplateResponse("dashboard.html", {"request": request, "complaints": complaints})


#this will mainly get me the logs regarding the timestamp, username, message
@app.post("/complaints/logs")
def create_complaint(complaint: ComplaintModel):
    logger.info(f"Complaint created by user: {complaint.user_id}")
    return {"msg": "Complaint logged"}


#this is just a mock of how the email is sent and no actual email is sent as of now. after this route is triggerd we go ahead with the hardcoded admin mail and then we get the messaged with the complaint part of the schema 
@app.post("/complaints/mail")
def create_complaint(complaint: ComplaintModel):
    send_email_notification(
        to_email="admin@example.com",
        subject="New Complaint Logged",
        body=f"A new complaint was submitted by {complaint.user_id}"
    )
    return {"msg": "Complaint created"}
