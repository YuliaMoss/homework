"""2- Create a class with a description of the worker. Any worker or employees."""


class WorkerDescription:
    """a class with a description of the worker"""

    def __init__(self, name: str, age: int, salary: int, city: str, job_title: str, department: str):
        """common information for worker

        Args:
            name (str): The name of the worker.
            age (int): The age of the worker.
            salary (int): The salary of the worker.
            city (str): The city where the worker is located.
            job_title (str): The job title of the worker.
            department (str): The department the worker belongs to."""
        self.name = name
        self.__age = age  # Private attribute
        self._city = city  # Protected attribute
        self.salary = salary
        self.title = job_title
        self.department = department
        self.__cart = {'card_number': 5468873390008122, 'cvv': 123, 'pin': 3456}

    def show_name(self):
        """Prints the name of the worker."""
        print(self.name)

    @classmethod
    def from_dict(cls, dict_worker: dict):
        """Creates a WorkerDescription object from a dictionary."""
        return cls(dict_worker.get('name'), dict_worker.get('age'), dict_worker.get('salary'),
                   dict_worker.get('city'), dict_worker.get('job_title'), dict_worker.get('department'))

    @property
    def age(self):
        """Getter for the age attribute."""
        return self.__age

    @property
    def city(self):
        """Getter for the city attribute."""
        return self._city

    def set_city(self, new_city: str = None):
        """Set a new city for the worker."""
        if new_city:
            self._city = new_city

    def __do_tasks(self):
        """Perform tasks related to the worker's job."""
        print(f'{self.name} does tasks')

    def __be_on_meetings(self):
        """Attend meetings related to the worker's job."""
        print(f'{self.name} is on meetings')

    def work_plan(self):
        """Execute the work plan, involving tasks and meetings."""
        self.__be_on_meetings()
        self.__do_tasks()

    def get_card_info(self):
        """Get information about the worker's card."""
        return self.__cart


if __name__ == '__main__':
    """Creating a worker object "Stepan" and setting its attributes"""
    stepan_dict = {'name': 'Stepan', 'age': 22, 'salary': 2000, 'city': 'Kyiv', 'job_title': 'Software Engineer',
                   'department': "Engineering"}
    stepan = WorkerDescription.from_dict(stepan_dict)

    """Displaying the worker's name"""
    stepan.show_name()

    print(stepan.city)
    """Changing the worker's city to "Lviv" and displaying the new city"""
    stepan.set_city('Lviv')
    print(stepan.city)

    """Getting and displaying information about the worker's card"""
    card_info = stepan.get_card_info()
    print("Card Info:", card_info)

    """Adding earnings to the salary"""
    stepan.salary += 500
    print("New Salary:", stepan.salary)
