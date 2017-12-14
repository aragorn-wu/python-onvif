from onvif import ONVIFCamera


class video(object):
    def getVideoInfo(self):
        mycam = ONVIFCamera(self.ip, self.port, self.administratorName, self.administratorPassword)
        media_service = mycam.create_media_service(False)
        media_service.