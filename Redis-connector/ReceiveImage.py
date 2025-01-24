import redis        # pip install redis
import io;
import base64

ip=""
r = redis.Redis(host=ip, port=6379, db=0,password='sofe4630u')

value=r.get('image');
decoded_value=base64.b64decode(value);

with open("./recieved.jpg", "wb") as f:
    f.write(decoded_value);
    
print('Image recieved, check ./recieved.jpg')
