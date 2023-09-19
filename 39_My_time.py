class Mytime():
    def __init__(self, seconds):
        self._hours = seconds // 3600  - seconds // 3600 // 24 * 24
        self._minutes =  (seconds - seconds // 3600 * 3600) // 60
        self._seconds = (seconds - seconds // 3600 * 3600)  - (seconds - seconds // 3600 * 3600)  // 60  * 60
        
    def get_hours(self):
        print(self._hours)
    
    def get_minutes(self):
        print(self._minutes)

    def get_seconds(self):
        print(self._seconds)
        
    def __str__(self):
        return f'{self._hours}:{self._minutes}:{self._seconds}'
            
    def __repr__(self):
        return f'{self._hours}:{self._minutes}:{self._seconds}'

