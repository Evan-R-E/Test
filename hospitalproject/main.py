import patient as p
import os

def searchPatientById():
    check = False
    patientID = str(input("Enter Patient ID: "))
    patientfile = open("hospitalproject/patients.txt", "r")

    for line in patientfile:
        if patientID in line:
            line = line.replace('_', ' ')
            print(line)
            check = True
    if check == False:
        print("Patient with ID ", patientID, "not in patient file")


def editPatientInfo():
    patientfile= open("hospitalproject/patients.txt", "r")
    patientfile1 = open ("temp.txt", "w")

    print ("\n")
    p.patient.id = (input ("Enter the patient id: "))
    print ("\n")

    lines = ' '
    while (lines):
        lines =patientfile.readline()
        line1 = lines.replace ("_", "  ")
        position = lines.split("_")
        if len(lines)>0:
            if (position[0]) == p.patient.id:
                print (line1)
                p.patient.name = input ("Enter new Name: ")
                p.patient.diagnosis = input ("Enter new diagnosis: ")
                p.patient.gender = input ("Enter new gender: ")
                p.patient.age = input ("Enter new age: ")
                patientfile1.write(p.patient.id+"_"+p.patient.name+"_"+p.patient.diagnosis+"_"+p.patient.gender+"_"+p.patient.age+"\n")
            else:
                patientfile1.write(lines)

    patientfile.close()
    patientfile1.close()
    os.remove("hospitalproject/patients.txt")
    os.rename("temp.txt", "hospitalproject/patients.txt")
    displayPatientsList()

def displayPatientsList():
    patientfile = open('hospitalproject/patients.txt', "r")
    for lines in patientfile:
        lines = lines.replace('_', ' ')
        print(lines)
    patientfile.close()

def addPatientToList():
    id = str(input("Enter patient ID:"))
    name = str(input("Enter patient name:"))
    diagnosis = str(input("Enter patient diagnosis:"))
    gender = str(input("Enter patient gender:"))
    age = str(input("Enter patient age:"))

    writePatientsListToFile(p.patient(id, name, diagnosis, gender, age))  

def writePatientsListToFile(patient):
    lines = [patient.id, "_", patient.name, "_", patient.diagnosis, "_", patient.gender, "_", patient.age]
    with open('hospitalproject/patients.txt', 'a') as f:
        f.writelines(lines)

def patientMenu():
    menunum = 1

    while menunum != 0:
        print("Patient Menu")
        print("0 - Return to Main Menu ")
        print("1 - Display Patient's List")
        print("2 - Search for Patient by UID")
        print("3 - Add Patient")
        print("4 - Edit Patient ")
        menunum = int(input("Enter Option:"))

        if(menunum == 1):
            displayPatientsList()    

        elif(menunum == 2):
            searchPatientById()

        elif(menunum == 3):
            addPatientToList()

        elif(menunum == 4):
            editPatientInfo()    

patientMenu()

