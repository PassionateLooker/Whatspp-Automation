from twilio.rest import Client 
 
account_sid = 'AC1581de2f28907d01bfe09e9f463c5b36' 
auth_token = 'd4b68dfd82b2cf5ae4c684e98044cdba' 
client = Client(account_sid, auth_token) 
# ff
def send_msg():

    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='jama jama jamaisu 😅😅',      
                              to='whatsapp:+918762987060' 
                          ) 
 
    print(message.sid)