import fetchai
import json
import requests
from database.db_interface import DatabaseInterface

class VerificationAgent:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config = json.load(file)
        self.db_interface = DatabaseInterface(self.config['db_config'])
    
    def perform_checks(self):
        print("Performing database integrity checks...")
        issues = self.db_interface.check_data_integrity()
        if issues:
            self.report_issues(issues)

    def report_issues(self, issues):
        reporting_url = self.config['reporting_agent_url']
        requests.post(reporting_url, json={'issues': issues})

if __name__ == '__main__':
    agent = VerificationAgent(config_file='config/config.json')
    agent.perform_checks()
