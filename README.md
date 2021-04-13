

<img src="assets/Avatar.png" width="75" height="75"> 

# DiscordArena 
Creating a Discord Game with a website

<img src="assets/classes/Bard.png" width="50" height="50"> <img src="assets/classes/Blacksmith.png" width="50" height="50"> 
<img src="assets/classes/Druid.png" width="50" height="50"> <img src="assets/classes/Mage.png" width="50" height="50"> 
<img src="assets/classes/Monk.png" width="50" height="50"> <img src="assets/classes/Paladin.png" width="50" height="50"> 
<br>
<img src="assets/classes/Priest.png" width="50" height="50"> <img src="assets/classes/Ranger.png" width="50" height="50"> 
<img src="assets/classes/Rogue.png" width="50" height="50"> <img src="assets/classes/Warlock.png" width="50" height="50"> 
<img src="assets/classes/Warrior.png" width="50" height="50"> <img src="assets/classes/Wizard.png" width="50" height="50"> 
<br>


# Development setup
Using: `Python 3.9`

### Run Api
`pip install -r api/requirements` Install requirements \
`docker-compose up` Start a development database \
`python -m api` Run Api

#### Default Postgres Settings 
`Username`: `postgres` \
`Password`: `postgres` \
`Connection`: `localhost:5432` \


### Run Bot
[Bot README.md](src/bot/README.md) \
`pip install -r bot/requirements` Install requirements\
`python -m bot` Run Bot



#### Known Issues

##### Windows
``` 
no matching manifest for windows/amd64 
in the manifest list entries
```
https://stackoverflow.com/a/51071057/13859228
