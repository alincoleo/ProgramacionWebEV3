from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route("/ejercicio2", methods=['GET','POST'])
def ejercicio2():
        if request.method =='POST':
            nombre1=request.form['nombre1']
            nombre2=request.form['nombre2']
            nombre3=request.form['nombre3']
            nombre=""
            largo=0
            for recorre in [nombre1,nombre2,nombre3]:
                if largo < len(recorre):
                    nombre = recorre
                    largo =len(recorre)
                elif largo == len(recorre):
                    nombre +=', '+ recorre
            if(largo>0):
                return render_template('ejercicio2.html',nombre1=nombre1,nombre2=nombre2,nombre3=nombre3,nombre=nombre,largo=largo)
        return render_template('ejercicio2.html')

@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
        if request.method =='POST':
            try:
                nota1=float(request.form['nota1'])
                nota2=float(request.form['nota2'])
                nota3=float(request.form['nota3'])
                asistencia=float(request.form['asistencia'])
                promedio=float(round((nota1+nota2+nota3)/3))
                if asistencia >=75 and promedio>=40:
                    return render_template('ejercicio1.html',nota1=nota1,nota2=nota2,nota3=nota3,promedio=promedio,asistencia=asistencia,estado='APROBADO')
                else:
                    return render_template('ejercicio1.html',nota1=nota1,nota2=nota2,nota3=nota3,promedio=promedio,asistencia=asistencia,estado='REPROBADO')                
            except :
                 error='error'
                 return render_template('ejercicio1.html',error=error) 
        return render_template('ejercicio1.html') 

#ejecucion en el servidor
if __name__ == '__main__':
    app.run(debug=True)
