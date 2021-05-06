# importing data set and saving each column in a list
import csv

ages = []
sexes = []
bmis = []
no_children = []
smokers = []
regions = []
ins_charges = []

# saving each value for all parameters in a specified list
with open('insurance.csv',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ages.append(row['age']),
        sexes.append(row['sex']),
        bmis.append(row['bmi']),
        no_children.append(row['children']),
        smokers.append(row['smoker']),
        regions.append(row['region']),
        ins_charges.append(row['charges'])

print(len(smokers))


class Insurance:
    def __init__(self, patient_ages, patient_sexes, patient_bmis, patient_no_children, patient_smokers, patient_regions,
                 patient_ins_charges):
        self.patient_ages = patient_ages
        self.patient_sexes = patient_sexes
        self.patient_bmis = patient_bmis
        self.patient_no_children = patient_no_children
        self.patient_smokers = patient_smokers
        self.patient_regions = patient_regions
        self.patient_ins_charges = patient_ins_charges

    # finding the average age of the patients in the dataset
    def average_age(self):
        sum_of_ages = 0
        for age in self.patient_ages:
            sum_of_ages += int(age)
        length = len(self.patient_ages)
        average = sum_of_ages / length
        print("Average age of patients is: " + str(round(average, 2)))

    # finding the unique regions of patients
    def unique_regions(self):
        no_regions = set(self.patient_regions)
        print(no_regions)

    # finding the average insurance charge for all patients
    def average_charge(self):
        sum_of_charges = 0
        for charge in self.patient_ins_charges:
            sum_of_charges += float(charge)
        average_charge = sum_of_charges / len(self.patient_ins_charges)
        print("The average charge per patient is: " + str(round(average_charge, 2)))

    # determining the number of smokers and non-smokers
    def smokers(self):
        patients_who_smoke = 0
        patients_who_dont = 0
        for smoker in self.patient_smokers:
            if smoker == 'yes':
                patients_who_smoke += 1
            else:
                patients_who_dont += 1
        print("The number of patients who smoke: " + str(patients_who_smoke))
        print("The number of patients who don't smoke:" + str(patients_who_dont))

    # creates a dictionary with attribute (age, sex, etc.) as key and all datapoints as values
    def create_dictionary_attribute(self):
        self.insurance_dict = {}
        self.insurance_dict['Age'] = self.patient_ages
        self.insurance_dict['Sex'] = self.patient_sexes
        self.insurance_dict['BMI'] = self.patient_bmis
        self.insurance_dict['Children'] = self.patient_no_children
        self.insurance_dict['Smoker'] = self.patient_smokers
        self.insurance_dict['Region'] = self.patient_regions
        self.insurance_dict['Ins_charges'] = self.patient_ins_charges
        return self.insurance_dict

    def create_dictionary_patient(self):
        self.patient_dict = {}
        for n in range(len(self.patient_ages)):
            self.patient_dict[n] = {'Age': self.patient_ages[n],
                                    'Sex': self.patient_sexes[n],
                                    'BMI': self.patient_bmis[n],
                                    'Children': self.patient_no_children[n],
                                    'Smoker': self.patient_smokers[n],
                                    'Region': self.patient_regions[n],
                                    'Ins_charges': self.patient_ins_charges[n]}
        return self.patient_dict

    # finding the difference in average costs for smokers and non-smokers
    def smoker_costs(self):
        smoker_charges = []
        non_smoker_charges = []
        # finds the index position of each value on
        for charge_index, charges in enumerate(self.patient_ins_charges):
            if self.patient_smokers[charge_index] == 'yes':
                smoker_charges.append(self.patient_ins_charges[charge_index])
            else:
                non_smoker_charges.append(self.patient_ins_charges[charge_index])

        total_smoker_charges = 0
        for value in smoker_charges:
            total_smoker_charges += float(value)
        average_smoker = total_smoker_charges / len(smoker_charges)

        total_non_smoker = 0
        for item in non_smoker_charges:
            total_non_smoker += float(item)
        total_charges = total_non_smoker
        average_non_smoker = total_non_smoker / len(non_smoker_charges)
        print("On average, smokers pay: " + str(round(average_smoker, 2)))
        print("On average, non-smokers pay: " + str(round(average_non_smoker, 2)))

    # The average age for someone who has at least one child in this dataset.
    def parent_ages(self):
        patient_parents = []
        for age_index, age in enumerate(self.patient_ages):
            if self.patient_no_children[age_index] >= '1':
                patient_parents.append(self.patient_ages[age_index])

        sum_of_parent_ages = 0
        for age in patient_parents:
            sum_of_parent_ages += int(age)
        average_age = sum_of_parent_ages / len(patient_parents)
        print("The average age of patients with one or more children is: " + str(round(average_age, 2)))

# initialising the Insurance class with made lists
patient_info = Insurance(ages, sexes, bmis, no_children, smokers, regions, ins_charges)

# dictionary for each attribute in the dataset
patient_info.create_dictionary_attribute()

# dictionary for each patient containing their information
patient_info.create_dictionary_patient()

# Average age of patients
patient_info.average_age()

# list of unique regions of each patient
patient_info.unique_regions()

# average insurance charge of all patients
patient_info.average_charge()

# number of patients who smoke and who don't
patient_info.smokers()

# average cost based on smoker status
patient_info.smoker_costs()

# average age of parents
patient_info.parent_ages()