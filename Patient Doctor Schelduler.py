SLOT_1 = '9:00AM'
SLOT_2 = '10:00AM'
SLOT_3 = '11:00AM'
SLOT_4 = '12:00PM'
SLOT_5 = '2:00PM'
SLOT_6 = '3:00PM'
SLOT_7 = '4:00PM'
SLOT_8 = '5:00PM'
SLOT_9 = '6:00PM'

CLASS_NAME = 'NAME'
CLASS_APPOINTMENT_INFO = 'APPOINTMENT_INFO'


class Patient(object):
    CLASS_ID = 'ID'
    CLASS_PREV_APPOINTMENTS = 'PREVIOUS_APPOINTMENTS'

    def __init__(self, f_name, l_name, ssn):
        self.f_name = f_name
        self.l_name = l_name
        self.ssn = ssn
        self.patient_name = self.f_name + " " + self.l_name
        self.patient_id = self.f_name[:1] + self.l_name + ssn
        self.patient_calendar = {
            CLASS_NAME: self.patient_name,
            self.CLASS_ID: self.patient_id,
            #self.CLASS_PREV_APPOINTMENTS: {},
            CLASS_APPOINTMENT_INFO: {}
        }
    def get_patient_record(self):
        patient_record =  {
            CLASS_NAME : self.patient_name,
            self.CLASS_ID : self.patient_id,
        }
        return patient_record

    def print_patient_calendar(self):
         print(self.patient_calendar)


class Doctor(object):
    CLASS_SPECIALITY = 'SPECIALITY'

    def __init__(self, f_name, l_name, speciality):
        self.f_name = f_name
        self.l_name = l_name
        self.doctor_name = self.f_name + " " + self.l_name
        self.speciality = speciality
        self.doctor_calendar = {
            CLASS_NAME: self.doctor_name,
            self.CLASS_SPECIALITY: self.speciality,
            CLASS_APPOINTMENT_INFO: {},
        }

    def get_doctor_record(self):
        doctor_record =  {
            CLASS_NAME : self.doctor_name,
            self.CLASS_SPECIALITY: self.speciality
        }
        return doctor_record

    def print_doctor_calendar(self):
        print (self.doctor_calendar)



class Scheduler(object):

    def schedule(self,doctor,patient,time):
        self.time = time
        self.doctor = doctor
        self.patient = patient
        if self.isdoctoravailable(doctor,time) and self.ispatientavailable(patient,time):
            self.update_patient_calendar(patient,doctor,time)
            self.update_doctor_calendar(patient,doctor,time)
            print ("Appointment Scheduled with Dr. " + doctor.doctor_name +  " for patient " + patient.patient_calendar[CLASS_NAME] + "\n")
            return True

    def isdoctoravailable(self,doctor,time):
        if doctor.doctor_calendar[CLASS_APPOINTMENT_INFO].has_key(time):
            print ("No Appointment Available with Dr. " + doctor.doctor_name + "\n")
            return False
        else:
            return True

    def ispatientavailable(self,patient,time):
        if patient.patient_calendar[CLASS_APPOINTMENT_INFO].has_key(time):
            print ("The patient " + patient.patient_name +  " already has an appointment with Dr. " + patient.patient_calendar[CLASS_APPOINTMENT_INFO][time][CLASS_NAME] + "\n")
            return False
        else:
            return True

    def update_patient_calendar(self,patient,doctor,time):
        patient.patient_calendar[CLASS_APPOINTMENT_INFO][time] = doctor.get_doctor_record()

    def update_doctor_calendar(self,patient,doctor,time):
        doctor.doctor_calendar[CLASS_APPOINTMENT_INFO][time] = patient.get_patient_record()


D1 = Doctor("Ryan", "Giggs", "Dental")
D2 = Doctor("Alex", "Fergusson","General")
P1 = Patient("Wayne", "Rooney", "1234")
P2 = Patient("Wayne", "Bridge", "1214")

S1 = Scheduler()
S1.schedule(D1,P1,SLOT_2)
S1.schedule(D1,P2,SLOT_1)

P1.print_patient_calendar()
P2.print_patient_calendar()

D1.print_doctor_calendar()
D2.print_doctor_calendar()