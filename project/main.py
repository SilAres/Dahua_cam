

from video_date import video_date, network_cam, ntp_cam
from dahua_functions import *
from creds import headers


cam = "192.168.1.108"
name = "cam1"
cam_new = "192.168.1.108"

network_cam["network.eth0.IPAddress"] = cam_new
network_cam["Network.Hostname"] = name

dahua_video(cam, headers, video_date)
dahua_ntp(cam, headers, ntp_cam)
dahua_name(cam, headers, name)
dahua_network(cam, headers, network_cam)
