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

class University:
    def __init__(self, name, accepted_note):
        self.name = name
        self.accepted_note = accepted_note
    
    def handle_application(self):
        if communication_queue:
            event = communication_queue.pop(-1)
            if isinstance(event, ApplicationSent):
                name = event.payload["name"]
                transcript_note = event.payload["transcript_note"]
                if transcript_note >= self.accepted_note:
                    payload = {"name":name, "transcript_note":transcript_note}
                    event = ApplicationAccepted(payload)
                    emmit_event(event)
                    print("{} got accepted to {} with the note {}".format(name, self.name, transcript_note))
                else:
                    payload = {"name":name, "transcript_note":transcript_note}
                    event = ApplicationRejected(payload)
                    emmit_event(event)
                    print("{} got rejected from {} with the note {}".format(name, self.name, transcript_note))
            else:
                print("unsupported event type")
                

