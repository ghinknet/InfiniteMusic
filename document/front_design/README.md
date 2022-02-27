# Front Design For GeSong System

## Content
### Before
### Front(User)
#### 1. Index Page
#### 2. Search Page
#### 3. History Page
#### 4. List Page
#### 5. Confirm Page
### Back(Admin)
#### 1. Access Page
#### 2. Audit Page
#### 3. List Page
#### 4. System Page

## Before
#### All template use WebApi to deal the operate
#### Recommand Vue.js, but you still can use jQuery(Ajax) :D
#### All Response Code (Int)
##### `10000` `Success`

## Front(User)

### Index Page
#### The index page use the root path ("/"),
#### Server will response a 301 code to jump to search page ("/search")

### Search Page
#### The search page use the path "/search"
#### A user have to log in to use the search function
#### WebApi Interface Detail:
##### Path: `/api/search`
##### Method: `POST`
##### Args:
###### `keyword` `string` `keyword of the song`
###### `token` `string` `user token`
##### Response Format: `Json`
##### Json Args: 
###### `code` `int` `response code`
###### `content` `list` `list of songs`
##### List of Songs Args(content):
###### `pid` `int` `platform id`
###### `id` `int` `song id(platform)`
###### `name` `string` `name of song`
###### `artists` `list` `list of artists`
###### `album` `dict` `album of this song`
###### `url` `string` `the media url of this song`
##### List of Artists Args:
###### `id` `int` `artist id(platform)`
###### `name` `string` `name of this artist`
###### `cover` `string` `image url of this aritist`
##### Album Args:
###### `id` `int` `album id(platform)`
###### `name` `string` `name of this album`
###### `cover` `string` `image url of this album`

### History Page
#### The history page use the path "/history"
#### Anybody can directly get history of songs
#### WebApi Interface Detail:
##### Path: `/api/history`
##### Method: `GET`
##### Args: `Nothing`
##### Response Format: `Json`
##### Json Args:
###### `code` `int` `response code`
###### `content` `list` `list of history songs`