import subprocess

def start_reporting_agent():
    subprocess.Popen(['python', 'agents/reporting_agent.py'])

def start_verification_agent():
    subprocess.Popen(['python', 'agents/verification_agent.py'])

if __name__ == '__main__':
    start_reporting_agent()
    start_verification_agent()
