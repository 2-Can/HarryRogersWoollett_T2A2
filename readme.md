# Song of The Year API

## Identification of the problem you are trying to solve by building this particular app. Why is it a problem that needs solving?
In many forms of entertainment, communities like to come together at the end of each year and discuss what art made an impact over the last 12 months. For avid music listeners it can be a real hassle keeping track of what you listen to, what's worth revisiting and what can be tossed away. So often after these discussions occur one will think "I can't believe I forgot to mention (x, y or z)!". Written notes get damaged or lost, and digitising them ends up with notes spread out over a million different notes apps. By using the Song of The Year API, users can upload the tracks they listen to, add them to unique playlists AND leave comments on other users' playlists to facilitate discussions -  all in one convenient location.

## Why have you chosen this database system. What are the drawbacks compared to others?
I've chosen PostgreSQL as the database managamenet system for this app, and there's many good reasons why. For starters, it's open-source and free to use. PostgreSQL uses familiar SQL syntax and is ACID-compliant, ensuring transactions made within the database are reliable. It also works natively on many of the most popular operating systems used today, and integrates with a huge number of programming languages.

Partly as a consequence of this wealth of features, PostgreSQL is noted as being slower than it's major competitors (such as MySQL) when dealing with large amounts of data. Additionally, as it's open-source there is less incentive to provide the documentation manuals in languages other than English.

## Identify and discuss the key functionalities and benefits of an ORM
An ORM or Object Relational Mapper allows users to manipulate a relational database using object-oriented programming languages, such as Python. It acts as a layer between the server and the database, translating Python functions into queries that can be interpreted by the database. This allows for greater ease of use, minimizing errors and expanding functionality. It allows us to make commands at scale, such as seeding a whole database or creating all our tables in one command, rather than inputting them individually. Many ORMs can also sanitize any queries made, removing the threat of SQL injections. In this project SQLAlchemy has been used as the ORM.

## Document all endpoints for your API

### Users LOGIN
*/auth/login*

Method: POST

Required data: Email and Password as raw JSON

Response: Email, authorization token, and is_admin True or False 

### Users REGISTER
*/auth/register*
Method: POST

Required data: 

Response: 

### Users GET
*/auth/*

Method:

Required data: 

Response: 

### Users DELETE
*/auth/user_id*

Method:

Required data: 

Response: 

### Playlists GET all

Method:

Required data: 

Response: 

### Playlists GET 1

Method:

Required data: 

Response: 

### Playlists POST

Method:

Required data: 

Response: 

### Playlists DELETE

Method:

Required data: 

Response: 

### Playlists PUT

Method:

Required data: 

Response: 

### Songs GET 1

Method:

Required data: 

Response: 

### Songs POST

Method:

Required data: 

Response: 

### Songs UPDATE

Method:

Required data: 

Response: 

### Songs DELETE

Method:

Required data: 

Response: 

### Comments POST

Method:

Required data: 

Response: 

### Comments DELETE

Method:

Required data: 

Response: 

### PlaylistSong POST

Method:

Required data: 

Response: 

### PlaylistSong DELETE

Method:

Required data: 

Response: 

## An ERD for your app

## Detail any third party services that your app will use

## Describe your projects models in terms of the relationships they have with each other

## Discuss the database relations to be implemented in your application

## Describe the way tasks are allocated and tracked in your project