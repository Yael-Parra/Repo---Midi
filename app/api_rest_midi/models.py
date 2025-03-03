from django.db import models

# Modelo Alumno
class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    alumno_nombre = models.CharField(max_length=50, verbose_name="Nombre del Alumno")
    alumno_apellidos = models.CharField(max_length=50, verbose_name="Apellidos del Alumno")
    alumno_fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return f"{self.alumno_nombre} {self.alumno_apellidos}"


# Modelo InfoPadresTutoresLegales
class InfoPadresTutoresLegales(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    mama_nombre = models.CharField(max_length=50, verbose_name="Nombre de la Madre")
    mama_apellido = models.CharField(max_length=50, verbose_name="Apellido de la Madre")
    mama_cedula = models.CharField(max_length=20, verbose_name="Cédula de la Madre")
    mama_telefono = models.CharField(max_length=20, verbose_name="Teléfono de la Madre")
    mama_email = models.EmailField(max_length=50, verbose_name="Email de la Madre")
    mama_empresa = models.CharField(max_length=100, verbose_name="Empresa de la Madre")
    papa_nombre = models.CharField(max_length=50, verbose_name="Nombre del Padre")
    papa_apellido = models.CharField(max_length=50, verbose_name="Apellido del Padre")
    papa_cedula = models.CharField(max_length=20, verbose_name="Cédula del Padre")
    papa_telefono = models.CharField(max_length=20, verbose_name="Teléfono del Padre")
    papa_email = models.EmailField(max_length=50, verbose_name="Email del Padre")
    papa_empresa = models.CharField(max_length=100, verbose_name="Empresa del Padre")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name="Alumno")

    def __str__(self):
        return f"Tutor de {self.id_alumno.alumno_nombre}"


# Modelo Terapeuta
class Terapeuta(models.Model):
    id_terapeuta = models.AutoField(primary_key=True)
    terapeuta_nombre = models.CharField(max_length=50, verbose_name="Nombre del Terapeuta")
    terapeuta_apellidos = models.CharField(max_length=50, verbose_name="Apellidos del Terapeuta")
    terapeuta_cedula = models.CharField(max_length=20, verbose_name="Cédula del Terapeuta")
    terapeuta_telefono = models.CharField(max_length=20, verbose_name="Teléfono del Terapeuta")
    terapeuta_email = models.EmailField(max_length=50, verbose_name="Email del Terapeuta")

    def __str__(self):
        return f"{self.terapeuta_nombre} {self.terapeuta_apellidos}"


# Modelo Colegio
class Colegio(models.Model):
    id_colegio = models.AutoField(primary_key=True)
    colegio = models.CharField(max_length=100, verbose_name="Nombre del Colegio")
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name="Alumno", null=True, blank=True)

    def __str__(self):
        return self.colegio


# Modelo Curso
class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    id_colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE, verbose_name="Colegio", null=True, blank=True)
    nombre_curso = models.CharField(max_length=100, verbose_name="Nombre del Curso", null=True, blank=True)

    def __str__(self):
        return self.nombre_curso


# Modelo Inscripcion
class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True, verbose_name="ID de Inscripción")
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name="Alumno")
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    id_colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE, verbose_name="Colegio", null=True, blank=True)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Inscripción")
    fecha_baja = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Baja")

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        unique_together = (('id_alumno', 'id_curso'),)  # Evita duplicados de inscripciones

    def __str__(self):
        return f"Inscripción {self.id_inscripcion} - {self.id_alumno.alumno_nombre} en {self.id_curso.nombre_curso}"


# Modelo Sesion
class Sesion(models.Model):
    id_sesion = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name="Alumno")
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    id_terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE, verbose_name="Terapeuta")
    fecha_sesion = models.DateTimeField(verbose_name="Fecha de Sesión")

    def __str__(self):
        return f"Sesión {self.id_sesion} - {self.id_alumno.alumno_nombre} con {self.id_terapeuta.terapeuta_nombre}"