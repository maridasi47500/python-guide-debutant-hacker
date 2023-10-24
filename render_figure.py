import re
class RenderFigure():
    def __init__(self,program):
        self.path=program.get_path()
        self.title=program.get_title()
        self.headingone=program.get_title()
        self.body=""
        


    def partie_de_mes_mots(balise="",text=""):
        r="<{balise}>{text}</{balise}>"
        s="""
        <html>
        <head>
        <title>{debutmots}</title>
        <h1>{mot}</h1>
        {plusdemots}
        </head>
        </html>
        """.format(debutmots=self.title, mot=self.headingone,plusdemots=self.body)
        return re.search(r, s)
    def debut_de_mes_mots(balise="div",text=""):
        r="<{balise}>{text}</{balise}>"
        s="""
        <html>
        <head>
        <title>{debutmots}</title>
        <h1>{mot}</h1>
        {plusdemots}
        </head>
        </html>
        """.format(debutmots=self.title, mot=self.headingone,plusdemots=self.body)
        return re.match(r, s)
    def fin_de_mes_mots(balise="div",text=""):
        r="<{balise}>{text}</{balise}>$"
        s="""
        <html>
        <head>
        <title>{debutmots}</title>
        <h1>{mot}</h1>
        {plusdemots}
        </head>
        </html>
        """.format(debutmots=self.title, mot=self.headingone,plusdemots=self.body)
        return re.search(r, s)
    def ajouter_a_mes_mots(self,balise,text):
        r="<{balise}>{text}</{balise}>"
        self.body+=r

    def render_figure(self,filename):
        
        self.body+=open(os.path.abspath(self.path+"/"+filename),"rb").read()
        return """
        <html>
        <head>
        <title>{debutmots}</title>
        <h1>{mot}</h1>
        {plusdemots}
        </head>
        </html>
        """.format(debutmots=self.title, mot=self.headingone,plusdemots=self.body)
