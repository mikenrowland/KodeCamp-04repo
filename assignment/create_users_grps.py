import subprocess

userGroups = {
    'sys_admins': ['Andrew'],
    'legal_team': ['Julius'],
    'hr_manager': ['Chizi'],
    'sales_managers': ['Jennifer'],
    'business_strategists': ['Adeola'],
    'company_execs': ['Bach'],
    'it_personnel': ['Gozie'],
    'finance_managers' : ['Ogochukwu']
}


def exec_cmd(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to exec command: {e}")

def create_groups():
    groups =  userGroups.keys()

    for group in groups:
        exec_cmd(f"sudo groupadd {group}")

    print(f"A total of {len(groups)} groups created.")

def create_user_and_add_group():
    for group, users in userGroups.items():
        for user in users:
            print(f"Creating user: {user}...")
            
            exec_cmd(f"sudo useradd -m -G {group} {user}")
            
            print(f"Added user {user} to {group}")


def main():
    print("Creating user profiles and groups...")

    create_groups()

    create_user_and_add_group()

    print("Process completed successfully.")


# Function call
main()


