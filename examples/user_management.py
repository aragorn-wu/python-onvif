from onvif import ONVIFCamera

if __name__ == '__main__':
    mycam = ONVIFCamera('10.10.16.19', 80, 'admin', 'admin123')
    devicemgmt_service = mycam.create_devicemgmt_service()

    users = devicemgmt_service.GetUsers()
    for user in users:
        if user.Username=="admin":
            user.Password="admin123"


    request = devicemgmt_service.create_type("SetUser")
    request.User = users
    request.ForcePersistence = False

    devicemgmt_service.SetUser(request)
