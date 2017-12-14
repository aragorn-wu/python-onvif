from onvif import ONVIFCamera


class Media(object):
    def __init__(self, ip, port, administratorName, administratorPassword):
        self.ip = ip
        self.port = port
        self.administratorName = administratorName
        self.administratorPassword = administratorPassword

    def getVideoInfo(self):
        mycam = ONVIFCamera(self.ip, self.port, self.administratorName, self.administratorPassword)
        media_service = mycam.create_media_service(False)
        ret = media_service.GetAudioSources()
        print(ret)


if __name__ == '__main__':
    media_service = Media('10.10.17.18', 80, 'admin', 'admin123')
    media_service.getVideoInfo()
