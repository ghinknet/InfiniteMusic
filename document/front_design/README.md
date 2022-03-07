# Front Design For InfiniteMusic System

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
### Public
#### 1. System Interface

## Before
#### All template use WebApi to deal the operate
#### Recommand Vue.js, but you still can use jQuery(Ajax) :D
#### All Response Code (Int)
##### `10000` `Success` `Successfully requested`
##### `20000` `No enough times` `No enough times to song`
##### `30000` `Forbidden` `Wrong Access (For User)`

## Front (User)

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
##### Cookie:
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
###### `url` `string` `the media url of this song (source platform or system cache)`
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
#### Anybody can directly get the history of songs
#### WebApi Interface Detail:
##### Path: `/api/history`
##### Method: `GET`
##### Args: `Nothing`
##### Response Format: `Json`
##### Json Args:
###### `code` `int` `response code`
###### `content` `list` `list of history songs`
##### List of Songs Args(content):
###### `pid` `int` `platform id`
###### `id` `int` `song id(platform)`
###### `name` `string` `name of song`
###### `artists` `list` `list of artists`
###### `album` `dict` `album of this song`
###### `url` `string` `the media url of this song (system cache)`
##### List of Artists Args:
###### `id` `int` `artist id(platform)`
###### `name` `string` `name of this artist`
###### `cover` `string` `image url of this aritist`
##### Album Args:
###### `id` `int` `album id(platform)`
###### `name` `string` `name of this album`
###### `cover` `string` `image url of this album`

### List Page
#### The list page use the path "/list"
#### Anybody can directly get the list of whitelist and blacklist
#### WebApi Interface Detail:
##### Path: `/api/list`
##### Method: `GET`
##### Args: `Nothing`
##### Response Format: `Json`
##### Json Args:
###### `code` `int` `response code`
###### `content` `dict` `dict of list, included whitelist and blacklist`
##### Content Dict(content):
###### `white` `list` `songs list of whitelist`
###### `black` `list` `songs list of blacklist`
##### List of Songs Args:
###### `pid` `int` `platform id`
###### `id` `int` `song id(platform)`
###### `name` `string` `name of song`
###### `artists` `list` `list of artists`
###### `album` `dict` `album of this song`
##### List of Artists Args:
###### `id` `int` `artist id(platform)`
###### `name` `string` `name of this artist`
###### `cover` `string` `image url of this aritist`
##### Album Args:
###### `id` `int` `album id(platform)`
###### `name` `string` `name of this album`
###### `cover` `string` `image url of this album`

### Confirm Page
#### The confirm page use the path "/confirm"
#### This page only use for the twice confirm
#### Located from the search page
#### Read the parameter from url on front code (Javascript)
#### Get Parameter:
##### `platform` `int` `platform id`
##### `id` `int` `id of the song`
#### Then use the id and platform id to requests the song detail
#### WebApi Interface Detail:
##### Path: `/api/detail`
##### Method: `POST`
##### Args: 
###### `platform` `int` `id of the platform`
###### `id` `int` `id of the song`
##### Cookie:
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
###### `url` `string` `the media url of this song (source platform or system cache)`
##### List of Artists Args:
###### `id` `int` `artist id(platform)`
###### `name` `string` `name of this artist`
###### `cover` `string` `image url of this aritist`
##### Album Args:
###### `id` `int` `album id(platform)`
###### `name` `string` `name of this album`
###### `cover` `string` `image url of this album`
#### After user clicking the confirm button, send request to this interface
#### WebApi Interface Detail:
##### Path: `/api/detail`
##### Method: `POST`
##### Args: 
###### `platform` `int` `id of the platform`
###### `id` `int` `id of the song`
###### `date` `string` `YYYY-MM-DD`
##### Cookie:
###### `token` `string` `user token`
##### Response Format: `Json`
##### Json Args: 
###### `code` `int` `response code`

## Back (Admin)

### Access Page
#### The access page use the path "/admin/access"
#### Only Admin can request this interface
#### Get list of user:
#### WebApi Interface Detail:
##### Path: `/api/userlist`
##### Method: `GET`
##### Cookie:
###### `token` `string` `user(admin operator) token`
##### Response Format: `Json`
##### Json Args: 
###### `code` `int` `response code`
###### `content` `list` `list of all users`
##### List of all users (content):
###### `uid` `int` `user id`
###### `nickname` `string` `user's nickname`
###### `name` `string` `user's real name (if realname auth passed)`
#### Request for change operate:
#### WebApi Interface Detail:
##### Path: `/api/admin/access`
##### Method: `POST`
##### Args: 
###### `token` `string` `user(admin operator) token`
###### `uid` `int` `user's id to change access`
###### `operate` `string` `admin or user, destination`
##### Response Format: `Json`
##### Json Args: 
###### `code` `int` `response code`

### Audit Page
#### The audit page use the path "/admin/audit/song" for song audit
#### Only Admin can request this interface
#### Get list of songs that songed by users
#### WebApi Interface Detail:
##### Path: `/api/auditlist/song`
##### Method: `GET`
##### Cookie:
###### `token` `string` `user(admin operator) token`
##### Response Format: `Json`
##### Json Args: 
###### `code` `int` `response code`
###### `content` `list` `list of all users`
##### List of songs that users songed (content):
###### `sid` `int` `id of this song(v.) event`
###### `uid` `int` `user id`
###### `nickname` `string` `user's nickname`
###### `name` `string` `user's real name (if realname auth passed)`
###### `platform` `int` `platform of the song`
###### `id` `int` `id of the song`
###### `name` `string` `name of song`
###### `artists` `list` `list of artists`
###### `album` `dict` `album of this song`
###### `url` `string` `the media url of this song (source platform or system cache)`
#### Request for audit operate:
#### WebApi Interface Detail:
##### Path: `/api/admin/listaudit`
##### Method: `POST`
##### Args: 
###### `token` `string` `user(admin operator) token`
###### `sid` `int` `id of this song(v.) event`
###### `operate` `string` `pass, abort or ignore`
##### Response Format: `Json`
##### Json Args: 
###### `code` `int` `response code`
#### The audit page use the path "/admin/audit/auth" for real name auth audit
#### Only Admin can request this interface
#### Get list of user's real name auth.
#### WebApi Interface Detail:
##### Path: `/api/auditlist/real`
##### Method: `GET`
##### Cookie:
###### `token` `string` `user(admin operator) token`
##### Response Format: `Json`
##### Json Args:
###### `code` `int` `response code`
###### `content` `list` `list of all real name auth requests`
##### List of real name auth requests (content):
###### `uid` `int` `id of the user`
###### `img` `string` `the url of the real name auth img`
###### `name` `string` `real name of the user`
#### Request for audit operate:
#### WebApi Interface Detail:
##### Path: `/api/admin/realaudit`
##### Method: `POST`
##### Argv:
###### `uid` `int` `id of the user that you audit`
###### `operate` `string` `pass or abort`
##### Cookie:
###### `token` `string` `user(admin operator) token`
##### Response Format: `Json`
##### Json Args: 
###### `code` `int` `response code`

### List Page
#### The list manage page use the path "/admin/list"
#### Only Admin can request this interface
#### Requests the public interface to get the list of blacklist songs and whitelist songs
##### `/api/list`
#### Request for list operate:
#### WebApi Interface Detail:
##### Path: `/api/admin/list`
##### Method: `POST`
##### Args: 
###### `sid` `int` `id of this song(v.) event`
###### `operate` `string` `white, black, remove`
##### Cookie:
###### `token` `string` `user(admin operator) token`
##### Response Format: `Json`
##### Json Args: 
###### `code` `int` `response code`

### System Page
#### The system control page use the path "/admin/system"
#### Only Admin can request this interface
#### Options:
##### `notice` `string` `System Notice`
##### `switcher` `bool` `Main switcher for the song function`
##### `igTime` `bool` ``Main switcher to ignore the time limit`
##### `timeRule` `list` `the timeRule setting`
#### timeRule look like:
``` [[6, "16:00:00", "23:59:59"], [0, "00:00:00", "8:00:00"]]```
#### 6 stand for Sat., and 0 stand for Sun.
#### I dont know how to design the form, everything depends on you guys :D
#### Get the setting now use the public interface: "System Interface"
#### Save the setting operate:
#### WebApi Interface Detail:
##### Path: `/api/admin/system`
##### Method: `POST`
##### Args: 
###### `OPTION` `TYPE` `NOTICE`
###### ```See the detail in options```
##### Cookie:
###### `token` `string` `user(admin operator) token`
##### Response Format: `Json`
##### Json Args: 
###### `code` `int` `response code`

## Public
### System Interface
#### Anybody can directly request this interface
#### Get system setting
##### WebApi Interface Detail:
##### Path: `/api/system`
##### Method: `GET`
##### Args: `Nothing`
##### Response Format: `Json`
##### Json Args:
###### `code` `int` `response code`
###### `content` `dict` `dict of list, included whitelist and blacklist`
##### Content Dict(content):
###### `notice` `string` `System Notice`
###### `switcher` `bool` `Main switcher for the song function`
###### `igTime` `bool` `Main switcher to ignore the time limit`
###### `timeRule` `list` `the timeRule setting`
##### List of time rule:
###### `0` `Index` `Index`
###### `1` `HH:MM:SS` `begin time`
###### `2` `HH:MM:SS` `end time`