import os
import sys

#constant for varify connection
FTRACK_CONNECTED = False

sys.path += ["D:/server/apps/3rdparty/ftrack-python"]

os.environ['FTRACK_SERVER'] = 'https://cas.ftrackapp.com'

import ftrack

FTRACK_CONNECTED = True


class Connector(object):
    """class for Connector
    Arg
        user(Optional[str]): user name,and user system username if None
    """

    def __init__(self, user=None):
        super(Connector, self).__init__()

        self.user = user
        self.userDetails = None
        self.UserTask = None

        if not self.user:
            self.user = os.environ['USERNAME']

    def getUser(self):
        return self.user

    def setUser(self, value):
        self.user = value

    def connect(self):

        os.environ['LOGNAME'] = self.user
        if  FTRACK_CONNECTED is True:
            print "Connection Successful!" 

    def getUserDetails(self):

        self.userDetails = ftrack.getUser(self.user)
        return self.userDetails

    def getUserDetails(self):

        self.userDetails = ftrack.getUser(self.user)
        return self.userDetails

    def getUserTask(self):

        userDetails = self.getUserDetails()

        self.UserTask = userDetail.getTasks()
        return self.userTasks 
        
