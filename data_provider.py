import csv

class DataProvider:
    @staticmethod
    def read_csv(file_path):
        with open(file_path, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            return [tuple(row) for row in reader]  # Convert to list of tuples

# Usage Example
if __name__ == "__main__":
    data = DataProvider.read_csv("data.csv")
    print(data)  # Output: [('user1', 'password1'), ('user2', 'password2'), ('user3', 'password3')]
