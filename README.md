# Employee Management System

A desktop application for managing employee records built with Python, Tkinter, and MySQL.

## Features

- **Admin Authentication**: Secure login system for administrators
- **User Management**: Add, view, and delete employee records
- **Employee Portal**: Employees can view their personal information
- **Database Integration**: MySQL database for persistent data storage
- **GUI Interface**: User-friendly interface built with Tkinter

## Technologies Used

- Python 3.x
- Tkinter (GUI)
- MySQL (Database)
- mysql-connector-python


## Installation

1. Clone this repository
2. Install MySQL and create a database named `employee_management`
3. Install required packages:
   ```bash
   pip install mysql-connector-python
   ```
4. Update database credentials in the code (host, user, password)
5. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. **Admin Login**: Sign up or log in as admin
2. **Add Employees**: Click "Add user" to register new employees
3. **View Details**: Employees can log in to view their information
4. **Delete Records**: Admins can remove employee records

## Database Schema

The application uses two main tables:
- `admin`: Stores admin credentials
- `employee`: Stores employee information (Name, ID, Password, DOB, Phone, Email)

## Future Improvements

- Add employee update functionality
- Implement password hashing for security
- Add search and filter options
- Export employee data to CSV/Excel

## Author

Dev Joshi - Python Developer

## License

This project is open source and available for educational purposes.
