# Role-Based Authentication (RBAC)

Today, I implemented Role-Based Access Control (RBAC) in the project. The system now supports two roles:  

- **Admin**  
- **User**  

The access to routes and functionalities is controlled based on these roles.

---

## Role-Based Authentication Setup

- Created a **Role** table.  
- Manually inserted roles (`admin`, `user`) into the database.  
- After the first registration, manually changed the first user’s role to **Admin**.  

---

## Admin Access Control

### Resource: User
- **User Registration** – Accessible by both Admin (to create user) and User  
- **Login System** – Accessible by both Admin and User  
- **Show All Users** – Only Admin can view users  
- **Delete User** – Only Admin can delete users  

### Resource: Project
- **Create Project** – Only Admin  
- **Show All Projects** – Accessible by both Admin and User (users see only assigned projects)  
- **Show Single Project** – Accessible by both Admin and User (users see only assigned project)  
- **Assign Project to User** – Admin assigns projects to users  

### Resource: Tasks
- **Create Task** – Only Admin  
- **Show Tasks** – Accessible by both Admin and User  
- **Update Task Status** – Both Admin and User can update task (e.g., Pending → Completed)  
- **Delete Task** – Only Admin can delete tasks  
