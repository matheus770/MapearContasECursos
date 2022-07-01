class ContaCurso:
    def __init__(self, sitename, email, cursos, logingoogle):
        self.sitename = sitename
        self.email = email
        self.cursos = cursos
        self.logingoogle = logingoogle
        
    def show(self):
        return f"site: {self.sitename} \nemail: {self.email} \ncursos: {self.cursos} \nlogingoogle: {self.logingoogle} \n"
    def to_Json(self):
        return{"site": self.sitename, "email": self.email, "cursos": self.cursos, "logingoogle": self.logingoogle}
    
    
    
    
    
    
    