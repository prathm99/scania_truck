from datetime import datetime


class App_Logger:
    def __init__(self):
        pass

    def log(self, file_object, log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_object.write(
            str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message +"\n")



#############################################################
#from datetime import datetime
# class App_logger():
#   def __init__(self):
        # pass
    # 
    # def logger(self, file_obj, msg):
        # self.now = datetime.now()
        # self.date = self.now.date()
        # self.time = self.now.strftime(%H:%M:%S)
        # file_obj.write(str(self.date)+"/"+str(self.time)+"\t\t"+msg+"\n")