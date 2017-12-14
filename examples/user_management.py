from onvif import ONVIFCamera


class User():
    def __init__(self, Username, Password, UserLevel):
        self.Username = Username
        self.Password = Password
        self.UserLevel = UserLevel

    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password


class UserManagement(object):
    def __init__(self, ip, port, administratorName, administratorPassword):
        self.ip = ip
        self.port = port
        self.administratorName = administratorName
        self.administratorPassword = administratorPassword

    def update_password(self, userName, newPassword):
        mycam = ONVIFCamera(self.ip, self.port, self.administratorName, self.administratorPassword)
        devicemgmt_service = mycam.create_devicemgmt_service(False)

        users = devicemgmt_service.GetUsers()

        updateUsers = []
        for user in users:
            if user.Username == userName:
                user.Password = newPassword
                updateUsers.append(user)

        request = devicemgmt_service.create_type("SetUser")
        request.User = updateUsers
        request.ForcePersistence = False

        devicemgmt_service.SetUser(request)


# '10.10.16.19', 80, 'admin', 'admin1234'
if __name__ == '__main__':
    usermgmt = UserManagement('10.10.16.19', 80, 'admin', 'admin123')
    usermgmt.update_password('admin', "admin123")
