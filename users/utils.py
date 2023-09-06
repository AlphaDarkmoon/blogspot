import os
import random

def get_random_profile_pic():
    profile_pic_dir = 'media/images/profile'  # Adjust the path as needed
    profile_pics = os.listdir(profile_pic_dir)
    if profile_pics:
        random_pic = random.choice(profile_pics)
        return f'{profile_pic_dir}/{random_pic}'
    return None
