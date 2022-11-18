# Song of The Year API - Harry RW 13184

[Github Repo](https://github.com/2-Can/HarryRogersWoollett_T2A2)

## Installation

1. Clone this Github repository
2. Create and activate a virtual environment in this folder
3. Install dependencies with the pip install `-r requirements.txt` command
4. Create a PSQL database to be used by the app
4. Rename the .env.sample file to just .env, and fill out the database connection & JWT secret key requirements within
5. Call the `flask db create` command in your terminal to build the databaes tables, and optionally use the `flask db seed` command to seed it with some entries to play around with. The `flask db drop` command can be used to clear the databse and start over.

## Identification of the problem you are trying to solve by building this particular app. Why is it a problem that needs solving?
In many forms of entertainment, communities like to come together at the end of each year and discuss what art made an impact over the last 12 months. For avid music listeners it can be a real hassle keeping track of what you listen to, what's worth revisiting and what can be tossed away. So often after these discussions occur one will think "I can't believe I forgot to mention (x, y or z)!". Written notes get damaged or lost, and digitising them ends up with notes spread out over a million different notes apps. By using the Song of The Year API, users can upload the tracks they listen to, add them to unique playlists AND leave comments on other users' playlists to facilitate discussions -  all in one convenient location.

## Why have you chosen this database system. What are the drawbacks compared to others?
I've chosen PostgreSQL as the database managamenet system for this app, and there's many good reasons why. For starters, it's open-source and free to use. PostgreSQL uses familiar SQL syntax and is ACID-compliant, ensuring transactions made within the database are reliable. It also works natively on many of the most popular operating systems used today, and integrates with a huge number of programming languages.

Partly as a consequence of this wealth of features, PostgreSQL is noted as being slower than it's major competitors (such as MySQL) when dealing with large amounts of data. Additionally, as it's open-source there is less incentive to provide the documentation manuals in languages other than English.

## Identify and discuss the key functionalities and benefits of an ORM
An ORM or Object Relational Mapper allows users to manipulate a relational database using object-oriented programming languages, such as Python. It acts as a layer between the server and the database, translating Python functions into queries that can be interpreted by the database. This allows for greater ease of use, minimizing errors and expanding functionality. It allows us to make commands at scale, such as seeding a whole database or creating all our tables in one command, rather than inputting them individually. Many ORMs can also sanitize any queries made, removing the threat of SQL injections. In this project SQLAlchemy has been used as the ORM.



## An ERD for your app
![SOTY ERD](docs/SOTY_ERD.PNG)
The ERD has a simple layout of 5 tables: Users, Playlists, Songs, PlaylistSongs and Comments.
A Users table is required to keep track of those who use the API, and connect them with their playlists. A unique user id is assigned to each user, and you’ll see this convention used with the entities in other tables. Having unique IDs for each entity also allows me to easily use them as primary and foreign keys, as noted in the ERD. A user can have many playlists but each playlist can only have one user, as there are no collaborative playlists available. The playlists table is used to connect the songs within the playlist to the user who created it. A separate Songs table contains all the specific song information of the tracks that users can place into their playlists. A join table called PlaylistSongs has been created to ensure we can track the actual contents of the playlists. Finally, the Comments table relates to both Users and Playlists. Each comment is made by only one user, and applies to only one playlist, however a user can make many comments and playlists can have multiple comments.


## Detail any third party services that your app will use
- **Flask**: A lightweight Python framework for making web apps.

- **SQLAlchemy**: The ORM that bridges the Python code and the PSQL database. Classes and functions in the program are translated to tables and statements in the database.

- **Marshmallow**: Assists with serializing and deserializing between SQLAlchemy models, standard Python data structures and JSON.

- **BCrypt**: Provides password-hashing functionality for additional security.

- **Postman**: An external program used to test and keep track of all API endpoints.

## Describe your projects models in terms of the relationships they have with each other
The models, relationships and schemas of my API have been constructed using SQLAlchemy and Marshmallow. Each entity model has a unique id, specified as a column with `primary_key=True` constraints. Similarly, foreign keys are created by placing a `ForeignKey` constraint on columns in related models. This allows us to easily connect between tables by sharing primary keys and foreign keys, and create child-parent relationships. Relationships are constructed between tables/models using the SQLAlchemy `relationship` function. This allows functionality such as the `back_populates` and `cascade` constraints, meaning that if an attribute is changed, added or removed on one entity, it is also changed, added or removed on the related entity. 

A clear display of these relationships can be seen in the Schemas, which utilise the `fields` function of Marshmallow. This allows me to nest the details of one entity inside another. For example, when I send a GET Users request, the playlists and comments made by the users are nested within the response.

Finally, data types are specified using constraints on each model's columns, such as Integer, String, Date or Text.

A summary of the models and their relationships is listed below:

- **User Model** relates to Playlists & Comments

- **Playlist Model** relates to Users(FK), Comments & Playlist Songs

- **Comments Model** relates to Users(FK) & Playlists(FK)

- **Song Model** relates to PlaylistSongs

- **PlaylistSong Model** relates to Playlists(FK) & Songs(FK)

## Discuss the database relations to be implemented in your application
The majority of relations being implemented in the application are One-to-Many. One user has many playlists, one Playlist has many PlaylistSongs, one Playlist has many Comments and so on. These have been established by creating a Primary Key - Foreign Key pairing between the tables. The keys used are the unique IDs attributed to each entry in each table. As they're forced to be unique, it ensures the validity of relationship - duplicated IDs would cause inaccuracies in the relationships. The cascading constraint of the relationships ensures these details are updated accordingly throughout the database.

## Describe the way tasks are allocated and tracked in your project
Tasks have been allocated and tracked using Trello, linked [here](https://trello.com/invite/b/pthtnIDx/ATTI91ce7fe6bd792a2380f9b665c70a4bd2550BB8A7/t2a2).

## Document all endpoints for your API

### Users LOGIN
*/auth/login*

**Method**: POST

**Required data**: "email" and "password" as raw JSON

**Response**: Email, authorization token, and is_admin (True or False)

### Users REGISTER
*/auth/register*

**Method**: POST

**Required data**: "first_name", "last_name", "email" and "password" as raw JSON

**Response**: "user_id", "first_name", "last_name", "email", "is_admin"

### Users GET
*/auth/users*

**Method**: GET

**Required data**: None

**Response**: User details, playlists and comments

### Users DELETE
*/auth/user_id*

**Method**: DELETE

**Required authentication**: Requires authenticated JSON Web Token 

**Response**: "User x deleted succesfully"

### Playlists GET All
*/playlists/*

**Method**: GET

**Required authentication**: Requires authenticated JSON Web Token

**Response**: List of all playlists, their songs and comments

### Playlists GET 1
*/playlists/playlist_id*

**Method**: GET

**Required authentication**: Requires authenticated JSON Web Token

**Response**: List of 1 playlist, its songs and comments

### Playlists CREATE
*/playlists/create*

**Method**: POST

**Required data**: "playlist_name" and "playlist_year" as raw JSON

**Required authentication**: Requires authenticated JSON Web Token

**Response**: Playlist details and details of user who created it.

### Playlists DELETE
*/playlists/playlist_id*

**Method**: DELETE

**Required authentication**: Requires authenticated JSON Web Token

**Response**: Playlist 'playlist_name' deleted succesfully

### Playlists UPDATE
*/playlists/playlist_id*

**Method**: PUT

**Required authentication**: Requires authenticated JSON Web Token

**Required data**: "playlist_name" and "playlist_year" as raw JSON

**Response**: Playlist with updated details, comments and songs.

### Songs GET
*/songs*

**Method**: GET

**Required authentication**: Requires authenticated JSON Web Token 

**Response**: List of all songs and song details in the database

### Songs GET 1
*/songs/song_id*

**Method**: GET

**Required authentication**: Requires authenticated JSON Web Token 

**Response**: Details of the specified song (name, artist, genre, album, year, duration, link)

### Songs CREATE
*/songs/create*

**Method**: POST

**Required authentication**: Requires authenticated JSON Web Token 

**Required data**: "song_name", "artist", "genre", "album", "song_year", "duration" and "song_link" as raw JSON

**Response**: All details of created song entry

### Songs UPDATE
*/songs/song_id*

**Required authentication**: Requires authenticated JSON Web Token 

**Required data**: One, many or all of the following details as raw JSON: "song_name", "artist", "genre", "album", "song_year", "duration" and "song_link"

**Response**: All details of updated song entry

### Songs DELETE
*/songs/song_id*

**Method**: DELETE

**Required authentication**: Requires authenticated JSON Web Token 

**Response**: Song 'song_name' deleted successfully

### Comments POST
*/playlists/playlist_id/comments*

**Method**: POST

**Required authentication**: Requires authenticated JSON Web Token 

**Required data**: "message" as raw JSON

**Response**: Playlist ID, User ID, Comment ID, message and date of creation.

### Comments DELETE
*/playlists/comments/comment_id*

**Method**:DELETE

**Required authentication**: Requires authenticated JSON Web Token 

**Response**: Comment 'message' deleted successfully

### PlaylistSong POST
*/playlists/playlist_id/song

**Method**: POST

**Required authentication**: Requires authenticated JSON Web Token 

**Required data**:  'song_id' as raw JSON

**Response**: song_id, playlist_id and playlistsongs_id

### PlaylistSong DELETE
*playlists/song/song_id*

**Method**:  DELETE

**Required authentication**: Requires authenticated JSON Web Token 

**Response**: Playlist song 'song_id' deleted successfully