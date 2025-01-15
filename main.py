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

communication_queue = []

def emmit_event(event):
    communication_queue.append(event)
    print("Event {} emitted".format(event.name))

class Student:
    def __init_(self, name, transcript_note):
        self.name = name
        self.transcript_note = transcript_note

    def apply_for_uni(self):
        payload = {"name":self.name, "transcript_note":self.transcript_note}
        event = ApplicationSent(payload)
        emmit_event(event)
        
