
class InicioPAM:
    @staticmethod
    def reglamentoPAM():
        
        reglamento = {
            1: "Se requiere 80% de asistencia para tener derecho a evaluación parcial y 80% de trabajos en clase.",
            2: "Se permiten 10 minutos de tolerancia y si el alumno llega después de este tiempo puede permanecer en la clase, pero no se tomará la asistencia (Solamente en los horarios de inicio:7:00a.m y 14:00 p.m).",
            3: "Las faltas deberán estar justificadas mediante el correo institucional con un plazo máximo de 24 horas posteriores a la hora de falta en clase mediante correo del tutor(a), justificantes entregados fuera de la fecha límite permitido no se aceptan, únicamente se aceptarán recetas médicas y citatorios jurídicos. (De forma física deben ser presentados al tutor para ser validados y de forma posterior emitidos).",
            4: "Las tareas y trabajos deberán subirlas al Classroom de forma individual y no se recibirán de manera extemporánea. (Salvo previo justificante validado por el tutor).",
            5: "Las tareas y trabajos presentarlos en tiempo y forma. La demora de un trabajo o tarea sin justificante y/o con justificante fuera del límite no se aceptan.",
            6: "Utilizar el correo institucional para trabajar bajo la plataforma Google Classroom.",
            7: "El plagio o copia de trabajos y/o exámenes, será condicionado a reprobar a la asignatura y se reportará al área correspondiente.",
            8: "Cualquier deshonestidad académica será sancionada reprobando el parcial sin derecho a examen final.",
            9: "En circunstancia de indisciplina o falta de respeto por parte del alumno hacia docentes, administrativos, compañeros o cualquier persona perteneciente a la universidad, se realizará una primera llamada de atención, si el alumno hace caso omiso tendrá que abandonar el aula, tres incidencias de este tipo el alumno no tendrá derecho a examen final o parcial.",
            10: "Uso de laptops y/o dispositivos móviles quedará limitados a uso exclusivo de las actividades que así lo requieran.",
            11: "Prohibido el uso de audífonos durante la clase.",
            12: "Prohibido comer y/o tomar líquidos en el salón.",
            13: "Prohibido sentarse encima de las mesas, así como columpiarse en las sillas.",
            14: "Todo tema académico debe ser revisado primeramente por parte del alumno con el docente, de no resolverse, pasar con su respectivo tutor, y de ser necesario con la coordinación de tutores. En caso de no solucionarse pasar a la dirección del programa educativo (debe mantenerse este seguimiento de forma obligatoria).",
            15: "Cualquier situación no prevista en el presente reglamento pasar directamente con la dirección del programa educativo.",
            16: "El día destinado a entrega de calificaciones todos los estudiantes deben estar presentes, ese día se entregarán exámenes y se brindará retroalimentación.",
            17: "Este reglamento entra en vigor después de que se firme o se acepte por la mayoría de los estudiantes asistentes a la primera sesión de la materia, una vez firmado o aceptado por el 50% más el jefe de grupo, es vigente para todo alumno inscrito en el curso aunque no esté presente en la primera sesión."
        }
        return reglamento
    

    @staticmethod
    def lineamientosClassRoom():
        lineamientos = {
            "1": "evidencia desempeño",
            "2": "PARTICIPACIÓN ACTIVA",
            "3": "TRABAJOS EN CLASSROOM: portada (diseño libre(logo UPQ, tema, datos del alumno, materia)) conclusión de aprendizaje (descripción de lo aprendido)",
            "4": "ENTREGAS COMPLETAS",
            "5": "RESPETAR TIEMPOS DE ENTREGA",
            "6": "PRESENTACIÓN DE TRABAJOS DE NIVEL UNIVERSITARIO"
        }

        return lineamientos

    
    @staticmethod
    def fechasDeParciales():
        fechasParciales = {
            "1er_parcial": "30-09-25",
            "2do_parcial": "04-10-25",
            "3er_parcial": "08-12-25"
        }

        return fechasParciales
    

    @staticmethod
    def porcentajesPorParcial():
        porcentajesParcial = {
            "1er_parcial": {
                "Evidencia de conocimiento": "40%",
                "Evidencia de desempeño": "20%",
                "Evidencia de producto": "30%",
                "Proyecto Integrador": "10%"
            },
            "2do_parcial": {
                "Evidencia de conocimiento": "40%",
                "Evidencia de desempeño": "20%",
                "Evidencia de producto": "20%",
                "Proyecto Integrador": "20%"
            },
            "3er_parcial": {
                "Evidencia de conocimiento": "20%",
                "Evidencia de desempeño": "10%",
                "Evidencia de producto": "40%",
                "Proyecto Integrador": "30%"
            }
        }

        return porcentajesParcial


