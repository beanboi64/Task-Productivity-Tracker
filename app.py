class TPT:
    def __init__(self):
        self.id = "Task-"
        self.tkNum = 0
        self.name = ''
        self.assigned_to = ''
        self.status = ''
        self.db = []
        
    def add_task(self):
        self.name = input('Enter Task Name: ')
        self.assigned_to = input('Enter Name To Assign Task: ')
        self.status = input('Enter status (e.g Urgent, Low, Medium): ')
        
        
    def save_task(self):
        self.new_db = {}
        self.tkNum += 1
        while True:
            
            if self.name == "":
                print("Error! Task cannot be left empty")
                self.name = input('Enter Task Name: ')
                continue
            
            if self.assigned_to == "":
                print("Error! Name cannot be left empty")
                self.assigned_to = input('Enter Name To Assign Task: ')
                continue
            
            if self.status == "":
                print("Error! Status cannot be left empty")
                self.status = input('Enter status (e.g Urgent, Low, Medium): ')
                continue
            
            if self.status.lower() not in ('urgent', 'low', 'medium'):
                print("Error! Enter a valid status (e.g Urgent, Low, Medium)")
                self.status = input('Enter status (e.g Urgent, Low, Medium): ')
                continue
            
            self.db.append({'id': f'{self.id}{self.tkNum}','name': self.name, 'assigned_to': self.assigned_to, 'status': self.status})
            
            break
        
        self.new_db = {task['id']: f"Task: {task['name']} | Assigned to: {task['assigned_to']}" for task in self.db if task['status'].lower() == 'urgent'}
        print(self.new_db)
        print(self.db)
    
    def report(self):
        self.reports = []
        self.tasks = ''
        print(f"+++Taks Per User+++")
        for user in self.db:
            self.reports.append(user['assigned_to'])
            #print(self.reports)
            
            if user['assigned_to'] in self.reports:
                self.tasks = self.reports.count(user['assigned_to'])
                
            print(f"Tasks: {self.tasks} User: {user['assigned_to']}")

myTracker = TPT()
myTracker.add_task()
myTracker.save_task()
myTracker.add_task()
myTracker.save_task()
myTracker.add_task()
myTracker.save_task()
myTracker.report()

