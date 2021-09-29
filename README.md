# drequests
drequests is a work in progress api wrapper for Discord's /v9/users/@me endpoint. Planning on adding more endpoints in the future. For now, this project is very useful for automating about me's and more.




# Example
```python
  from API import drequests, Endpoints as e

  auth = "DISCORD_TOKEN"
  
  username = drequests.get(e.username, auth)
  discriminator = drequests.get(e.discriminator, auth)
  print(f"{username}#{discriminator}")
  
  
  
  # Change About Me #

  drequests.patch(e.bio, "This is the new about me text", auth)
  newbio = drequests.get(e.bio, auth) # Print out the new about me
  print(newbio)
```
