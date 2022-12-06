class patient():

    def __init__(patient, id, name, diagnosis, gender, age):
        patient.id = id
        patient.name = name
        patient.diagnosis = diagnosis
        patient.gender = gender
        patient.age = age
        
    def formatPatientInfo(patient):
        return f"{patient.id}_{patient.name}_{patient.diagnosis}_{patient.gender}_{patient.age}"

    def __str__(patient):
        return f"{patient.id <5}{patient.name: <15}{patient.gender: <15}{patient.age: <5}"


