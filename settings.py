def getSettings():
    if not Settings.settings:
        Settings.settings = Settings()
    return Settings.settings

class Settings(object):
    settings = None
    _PATH = 'settings.properties'
    _DEFAULT = {
                'API.Host'          : 'localhost',
                'API.Port'          : '8080',
                'API.AddMember'     : 'api/groups/%s/members/add',
                'API.AttendEvent'   : 'api/groups/%s/events/%s/attend/attend',
                }
    
    def __init__(self):
        self.kv = {}
        for (k, v) in Settings._DEFAULT.items():
            self.kv[k] = v
        self.load()
        self.save()
    
    def parseBoolean(self, key):
        if self.kv.has_key(key):
            if self.kv[key].strip() == 'False':
                return False
            elif self.kv[key].strip() == 'True':
                return True
        return None
    
    def parseString(self, key):
        if self.kv.has_key(key):
            return str(self.kv[key]).strip()
        return None
    
    def parseInt(self, key):
        if self.kv.has_key(key):
            try:
                return int(self.kv[key].strip())
            except:
                return None
        return None
    
    def setValue(self, key, value):
        self.kv[key] = str(value)
        self.save()
    
    def save(self):
        try:
            io = open(Settings._PATH, 'w')
            for k, v in self.kv.items():
                io.write('{0}={1}'.format(k, v).strip() + '\n')
        finally:
            io.close()
    
    def load(self):
        io = None
        try:
            io = open(Settings._PATH, 'r')
            while True:
                r = io.readline()
                if r == '':
                    break
                spl = r.split('=')
                k, v = spl[0], spl[1]
                self.kv[k] = v
        finally:
            io.close()