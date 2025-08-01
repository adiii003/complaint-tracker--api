import logging

#used to keep the track of data and it prints the status with the severity and makes sure that all are shown at the logs , it is mainly about the program and you can share logs to your email as well
logging.basicConfig(
    level=logging.INFO, #this is the level as we can add the severity as error, infor and etc
    format="%(asctime)s - %(levelname)s - %(message)s", #this is the format you want your data to be in the output
    filename="app.log", #the logs are written to a file named log and it is created if it doesn't exist
    filemode="a", #this is the file mode which is append mode and it keeps on adding data and we can make it "w" to overwrite the data whenever we want to
)

#this part is to mainly store the module name with the help of "__name__" as we will not need to mention it always
logger = logging.getLogger(__name__)
