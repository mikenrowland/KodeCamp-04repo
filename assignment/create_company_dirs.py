import os

companyDirs = [
    'finance_budgets',
    'contract_docs',
    'business_projections',
    'business_models',
    'employee_data',
    'company_vision_mission',
    'system_configs'
]

homeDir = "company_docs"

def create_dirs():
    if not os.path.exists(homeDir):
        os.makedirs(homeDir)

    for _dir in companyDirs:
        dirPath = os.path.join(homeDir, _dir)

        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
            print(f"{dirPath} has been created")
        else:
            print(f"{dirPath} already exists in {homeDir}")


    print("Process completed successfully.")


# Create file functionality
def create_company_files(dirName, fileName):
    if dirName not in companyDirs:
        print(f"Invalid directory")
        return
    
    dirPath = os.path.join(homeDir, dirName)
    filePath = os.path.join(dirPath, fileName)

    if not os.path.exists(filePath):
        with open(filePath, 'w') as f:
            f.write("")
        print(f"{filePath} created")
    else:
        print(f"Error! {filePath} already exists.")


# Function call
create_dirs()


fileToCreate = input("Enter name of file to create: ")
dirForFile = input("Enter name of directory to add file: ")

create_company_files(dirForFile, fileToCreate)
