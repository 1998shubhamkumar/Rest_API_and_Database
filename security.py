from user import User 
from werkzeug.security import safe_str_cmp



def auth(username,password): #THIS method provide us authentication 
    user = User.find_by_username(username,None) #THIS provide us the username 
    if user and safe_str_cmp(user.password,password):  #COMPARE THE USER AND USERNAME WITH THEIR PASSWORD if alredy registered then return the user
        return user

def identity(payload):   
    id = payload['identity']
    return User.find_by_id(id) 