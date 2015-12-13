from PythonQt.QtCore import QFile
from PythonQt.QtGui import QDesktopServices, QMessageBox
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import ScreenCloud
import httplib
import urllib2
import json


class VgyUploader():

    def __init__(self):
        pass

    def showSettingsUI(self, parentWidget):
        QMessageBox.information(parentWidget,
                                'Vgy',
                                'This plugin has no settings.')

    def isConfigured(self):
        return True

    def getFilename(self):
        return ScreenCloud.formatFilename('Screenshot')

    def upload(self, screenshot, name):

        temp = QDesktopServices.storageLocation(QDesktopServices.TempLocation)
        file = temp + '/' + name

        screenshot.save(QFile(file), ScreenCloud.getScreenshotFormat())

        register_openers()

        datagen, headers = multipart_encode({'file': open(file, 'rb')})
        req = urllib2.Request('https://vgy.me:443/upload', datagen, headers)

        res = json.loads(urllib2.urlopen(req).read())

        ScreenCloud.setUrl(res['url'])
        return True
