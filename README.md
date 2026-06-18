
# Intelligence Task Manager

Intelligence Task Manager is a system designed for ShadowNet to manage their agents and missions.

## directory structure:

```plaintext
Intelligence-Task-Manager/
├── main.py
├── database/
│   ├── db_connection.py
│   ├── agent_db.py
│   └── mission_db.py
├── database/
│   ├── agent_routes.py
│   ├── mission_routes.py
│   └── report_routes.py
├── models/
│   ├── mission_create_model.py
│   ├── mission_view_model.py
│   ├── agent_create_model.py
│   ├── agent_update_model.py
│   ├── types.py
│   └── agent_view_model.py
├── .env
├── .env.example
├── logs/
│   └── app.log
├── README.md
├── requirements.txt
└── .gitignore
```

## data structures - tables:

### Agents:

| field              | type                                            | notes                                                                 |
| ------------------ | ----------------------------------------------- | --------------------------------------------------------------------- |
| id                 | INT, AUTO_INCREMENT, PK                         | Unique identifier.                                                    |
| name               | VARCHAR(50), NOT NULL                           | the agent's name                                                      |
| specialty          | VARCHAR(50), NOT NULL                           | the agent's specialty domain                                          |
| is_active          | BOOLEAN, DEFAULT TRUE                           | is this an active agent?                                              |
| completed_missions | INT, DEFAULT 0                                  | how many **successfully** completed missions has this agent done |
| failed_missions    | INT, DEFAULT 0                                  | how many **failing** completed missions has this agent done     |
| agent_rank         | ENUM('Junior', 'Senior', 'Commander'), NOT NULL | the agent's rank                                                      |

### Missions:

| field             | type                       | notes                                                                          |
| ----------------- | -------------------------- | ------------------------------------------------------------------------------ |
| id                | INT, AUTO_INCREMENT, PK    | Unique identifier.                                                             |
| title             | VARCHAR(50), NOT NULL      | moission's title                                                               |
| description       | TEXT, NOT NULL             | a comprehensive description of the mission                                     |
| location          | VARCHAR(50), NOT NULL      | where is this mission taking place?                                            |
| difficulty        | INT, NOT NULL              | 1 - 10 only                                                                    |
| importance        | INT, NOT NULL              | 1 - 10 only                                                                    |
| status            | VARCHAR(11), DEFAULT 'NEW' | mission's status, defaults to 'NEW'                                            |
| risk_level        | VARCHAR(8)                 | the mission's risk level. auto calculated based on difficulty and importance. |
| assigned_agent_id | INT                        | holds the assigned agent's id, NULL until assigned                             |

 risk_level calculation formula: difficulty * 2 + importance.

risk_level mapping: LOW: 0-9, MEDIUM: 10-17, HIGH: 18-24, CRITICAL: 25+

mission statusses: NEW, ASSIGNED, IN_PROGRESS, COMPLETED, FAILED, CANCELLED.

## classes:

### DBConnection:

a class that allows you to coonect to and manage the Database server.

it has three main methods:

`get_connection()`: returns an active connection to the database or server, user must close.

`create_database()`: creates the database if it does not already exist name defaults to 'Intelligence_db'.

`create_tables()`: creates the 'missions' and 'agents' tables in the database (defaults to 'Intelligence_db') if they do not already exist.

in addition it also has a constructor that takes 'host', 'port', 'user', 'password', 'database'. all arguments must be passed by name and all of them are optional with defaults.

also every instance of this class can act as a context manager yeilding a cursor and closing and commiting it afterwards.

### AgentDB:

this class manages the 'agents' table.

it has the following methods:

`create_agent(data)`: create's a new agent and returns the newly created agent's object (AgentView).

`get_all_agents()`: returns a list of all agents or an empty list if none exist.

`get_agent_by_id(id)`: returns a spesific agent by its id or `None` if no such agent exists.

`update_agent(id, data)`: update's the agent with a matching id setting its data to data (Note: that you can not chande the id itself!), returns a success \ failure message.

`deactivate_agent(id)`: deactivates the agent with a matching id, returns a success \ failure message.

`increment_completed(id)`: increments an agent's completed mission count, returns a success \ failure message.

`increment_failed(id)`: increments an agent's failed mission count, returns a success \ failure message.

`get_agent_performance(id)`: returns a dictionary of the folowing structure:

```json
{
    "total":0,  // the total amount of missions assigned to this agent.
    "failed":0,  // the total amount of missions this agent failed to complete.
    "completed":0,  // the total amount of missions completed by this agent.
    "success_rate":0  // the success rate for this agent.
}
```

`count_active_agents()`: returns the number of currently active agents.

### MissionDB:

`create_mission(data)` : creates a new mission and returns the newly created mission's object (MissionView)

`get_all_missions()` : returns a list of all missions or an empty list if no missions exist.

`get_mission_by_id(id)`: returns a spesific mission's object by its id. `None` if it doesn't exist.

`assign_mission(m_id, a_id)`: assigns a mission to an agent, returns a success \ failure message.

`update_mission_status(id, status)`: update the status of a mission by the mission's id to a given status, returns a success \ failure message.

`get_open_missions_by_agent(id)`: returns a list of all open missions (ASSIGNED \ IN_PROGRESS) assigned to the agent with id.

`count_all_missions()`: returns the total count of all missions.

`count_by_status(status)`: returns the total count of missions with a given status.

`count_open_missions()`: returns the total count of open missions.

`count_critical_missions()`: returns the total count of critical missions.

`get_top_agent()`: returns the agent whom has completed the most missions.

### MissionCreateModel:

A pydantic model class.
holding the data needed to create a new mission.

### MissionViewModel:

A pydantic model class.
holding the data avilable for a mission.

### AgentCreateModel:

A pydantic model class.
holding the data needed to create a new agent.

### AgentViewModel:

A pydantic model class.
holding the data avilable for an agent.

### AgentUpdateModel:

A pydantic model class.
holding the data needed to update an agent (all optional but at least one field set, no id.)

## Endpoints:

### agent endpoints:
1. POST /agents      - create a new agent.
2. GET  /agents      - get all agents.
3. GET  /agents/{id} - get an agent by it's id.
4. PUT  /agents/{id} - update an agent's data.
5. PUT  /agents/{id}/deactivate - deactivate (retire) an agent.
6. GET  /agents/{id} - get the performance summary of this agent.

### mission endpoints:
1. POST /missions - create a new mission.
2. GET /missions - get all missions.
3. GET /missions/{id} - get a mission by it's id.
4. PUT /missions/{id}/assign/{agent_id} - assign a mission to an agent.
5. PUT /missions/{id}/start - start a mission (status = 'IN_PROGRESS').
6. PUT /missions/{id}/complete - successful completion of the mission.
7. PUT /missions/{id}/fail - failing completion of the mission.
8. PUT /missions/{id}/cancel -  cancel the mission.


### report endpoints:
1. GET summary/reports/ - get a summary of the system's status in the folowing format:
```json
{
"active_agents_count": 0,
"total_missions": 0,
"open_missions": 0,
"completed_missions": 0,
"failed_missions": 0,
"critical_missions": 0
}
```
2. GET /reports/missions-by-status - get a count of how many missions are under each status.
3. GET /reports/top-agent - get the agent who completed the most missions.

## system rules:

1. **valid ranks** - a rank field can only contain one of the folowing values ('Junior', 'Senior', 'Commander'). any other value raises an error.
2. **difficulty & importance scope** - both difficulty and importance fields must stay between 1 and 10.
3. **risk_level source** - the risk_level field is never supplied by the user it is always calculated by the system as mentiond above.
4. **inactive agents** - an inactive agent can not have new missions assigned to him.
5. **maximum open missions per agent** - an agent can't have more than 3 open missions assigned to him.
6. **minimum rank for critical missions** - the minimal rank needed for a critical mission is a Commander rank meaning otherwise ranked agents cann not be assigned to critical missions.
7. **mission assignment stage** - you can only assign a mission if it is currently in the 'NEW' status, after you assign it its status needs to be 'ASSIGNED'.
8. **mission execution rule** - you can only start a mission if it is in the 'ASSIGNED' status, doing so means changing its status to 'IN_PROGRESS'.
9. **mission completion rule** - you can only complete a mission if its status is 'IN_PROGRESS' after doing so status changes to either 'COMPLETED' or 'FAILED'. 
10. **mission cancelation rule** - you can only cancle a mission if its status is either 'NEW' or 'ASSIGNED', doing so means changing the status to 'CANCELLED'.

## How to run:
first clone this repo:
```bash
git clone https://github.com/ariWeinberg/Intelligence-Task-Manager.git
```
open (move into) the new folder:
```bash
cd ./Intelligence-Task-Manager
```
start the mysql database:
```bash
docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 \
    -e MYSQL_DATABASE=Intelligence_db -p 3406:3306 mysql:8.0
```
NOTE: that i used a port other than what was specified in th exam spesification beacause i have a local system (probably some system package) running on this port.
if you want to use another port you are free to do so and to make the code use such a port you have to pass it to the DBConnection class on every instantiation.

install all dependencies:
```bash
pip install -r ./requirements.txt
```

start the server:
on linux (ubuntu):
```bash
python3 ./main.py
```
on windows:
```bash
py ./main.py
```

#### note:
if you want to override the default port, host, or db settings you can do so by setting them in the .env file.  
see .env.example file for an example.
