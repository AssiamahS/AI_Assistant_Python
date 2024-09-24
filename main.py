import datetime

class AIAssistant:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name, deadline):
        deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        self.tasks[task_name] = deadline_date
        return f"Task '{task_name}' added with deadline {deadline_date}."

    def remove_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            return f"Task '{task_name}' removed."
        else:
            return "Task not found."

    def get_upcoming_tasks(self):
        now = datetime.datetime.now()
        upcoming_tasks = {task: deadline for task, deadline in self.tasks.items() if deadline > now}
        return upcoming_tasks

    def remind_tasks(self):
        now = datetime.datetime.now()
        reminders = []
        for task, deadline in self.tasks.items():
            if now >= deadline - datetime.timedelta(minutes=30) and now < deadline:
                reminders.append(f"Reminder: Task '{task}' is due at {deadline}.")
        return reminders

# Example usage
assistant = AIAssistant()
print(assistant.add_task("Finish report", "2024-09-25 14:00"))
print(assistant.add_task("Team meeting", "2024-09-24 17:00"))
print(assistant.get_upcoming_tasks())
print(assistant.remind_tasks())
