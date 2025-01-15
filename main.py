class Event:
    def __init__(self, payload):
        self.payload = payload
        
class ApplicationSent(Event):
    name = "applicaiton_sent"
    def __init__(self, payload):
        super().__init__(payload)

class ApplicationAccepted(Event):
    name = "application_accepted"
    def __init__(self, payload):
        super().__init__(payload)

class ApplicationRejected(Event):
    name = "application_rejected"
    def __init__(self, payload):
        super().__init__(payload)
   
