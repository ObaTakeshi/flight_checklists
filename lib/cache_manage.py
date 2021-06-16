import os

class CacheManage:

    @staticmethod
    def flash():
        with open(os.environ['alfred_workflow_data'], 'w') as f:
            f.write('')

    @staticmethod
    def read():
        with open(os.environ['alfred_workflow_data'], 'r') as f:
            row_checklist = f.readlines()

        row_checklist = [x.replace('\n', '') for x in row_checklist if not x == '']

        return row_checklist

    @staticmethod
    def write(row_checklist):
        with open(os.environ['alfred_workflow_data'], 'w') as f:
            f.writelines('\n'.join(row_checklist))

    @staticmethod
    def make_checklist(query):
        with open(query, 'r') as f:
            row_checklists = f.readlines()

        checklists = [x.replace('\n', '') for x in row_checklists if not x == '']

        with open(os.environ['alfred_workflow_data'], 'w') as f:
            f.writelines('\n'.join(checklists))
