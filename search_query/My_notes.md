Search Query in FastAPI 
What is a Search Query? 
A search query is a way for users to filter data based on keywords or conditions. 
Example: 
When you type "john" in an admin dashboard to find a user → that "john" is the search query. 
In APIs, it’s sent as a query parameter in the URL: 
GET /users?search=john 
/users?search=john&page=2 
└──────────────┘ 
Query String 
● Starts with ? 
● Key-value pairs: key=value 
● Multiple parameters separated by & 
● Handled in FastAPI using Query() from fastapi 
How to Use Query Parameters in FastAPI 
from fastapi import Query 
def get_users( 
search: str = Query(None, description="Search by username or email"), 
page: int = Query(1, ge=1), 
size: int = Query(10, gt=0, le=100) 
): 
Where 
search: str = Query(None)  is Optional search term 
% = wildcard (any number of any characters 
How Search Works in the Database (SQLAlchemy) 
You used this code: 
if search: 
query = query.filter( 
(User.username.ilike(f"%{search}%")) | 
(User.email.ilike(f"%{search}%")) 
) 
if search: 
Only apply the filter if the user provided a search term. 
● If search = None or empty → skip 
● Prevents unnecessary filtering 
2. .filter() 
Narrows down the database query. 
● db.query(User) → gets all users 
● .filter(condition) → returns only matching rows 
Equivalent to SQL: 
SELECT * FROM users WHERE username ILIKE '%ali%' OR email ILIKE '%ali%'; 
3. .ilike() 
Case-insensitive pattern match (PostgreSQL, SQLite) 
User.username.ilike("%pattern%") 
% = wildcard (any number of any characters) 
Users: 
Search by username or email 
Project 