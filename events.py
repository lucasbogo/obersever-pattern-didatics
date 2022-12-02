# List of functions that need to be invoked whenever this event actually happens
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class Person: 
    def __init__(self, name, address) :
        self.name = name
        self.address = address
        # Event for a person's specific illness. That way a Doctor can subscribe to this event to receive a notification whenever a patient get this specific ilness
        self.falls_ill = Event()
    
    # Method for catching a cold
    def catch_a_cold(self):
        # Event declared in line 14 with the argument catch_a_cold passed in
        self.falls_ill(self.name, self.address)
        
# The Doctor wants to be notified whenever a person catches a cold
def call_doctor(name, address):
    print(f'{name} needs a doctor at {address}')
    
# Make sure whenever a person falls ill, the doctor gets called
if __name__ == '__main__':
    person = Person('Lucas', 'Rua Biguacu 580')
    # Subscribe to an event using lambda
    person.falls_ill.append(
        lambda name, address: print(f'{name} is ill')
    )
    # Call doctor when a person falls ill
    person.falls_ill.append(call_doctor)
    # Simulate a person catching a cold
    person.catch_a_cold()
    
    # Remove call_doctor (if the person just took too many drugs, a doctor might not want to be called. Just sleep it off, my dude!)
    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()
    

    
    
     