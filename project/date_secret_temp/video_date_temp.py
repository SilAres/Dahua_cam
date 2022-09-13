video_date= {"Encode[0].MainFormat[0].Video.resolution":"1280x960",
"Encode[0].MainFormat[0].Video.BitRate":"1024",
"Encode[0].MainFormat[0].Video.BitRateControl":"CBR",
"Encode[0].MainFormat[0].Video.Compression":"H.265",
"Encode[0].MainFormat[0].Video.CustomResolutionName":"2560x1440",
"Encode[0].MainFormat[0].Video.FPS":"6",
"Encode[0].MainFormat[0].Video.GOP":"12",
"Encode[0].ExtraFormat[0].Video.resolution":"704x576",
"Encode[0].ExtraFormat[0].Video.BitRate":"512",
"Encode[0].ExtraFormat[0].Video.BitRateControl":"CBR",
"Encode[0].ExtraFormat[0].Video.Compression":"H.265",
"Encode[0].ExtraFormat[0].Video.FPS":"25",
"Encode[0].ExtraFormat[0].Video.GOP":"50"
                  }

audio_enable_date= {"Encode[0].ExtraFormat[0].AudioEnable" : "true",
"Encode[0].MainFormat[0].AudioEnable" : "true",
"Encode[0].MainFormat[1].AudioEnable" : "true",
"Encode[0].MainFormat[2].AudioEnable" : "true",
"Encode[0].MainFormat[3].AudioEnable" : "true"
                  }



network_cam = {
"Network.eth0.DefaultGateway": "10.1.1.2",
"Network.eth0.IPAddress" : "10.1.1.1",
"Network.eth0.SubnetMask" : "255.255.255.0",
"Network.Hostname" : "Name"
}



ntp_cam = {
    "NTP.Address":"10.1.1.1",
    "NTP.Enable":"true",
    "NTP.Port":"123",
    "NTP.TimeZone":"3",
    "NTP.TimeZoneDesc":"Moscow",
    "NTP.UpdatePeriod":"10"
}
