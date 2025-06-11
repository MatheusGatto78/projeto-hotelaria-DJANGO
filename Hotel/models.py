from django.db import models

class homepage(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    logo = models.ImageField(upload_to='homepage/')

    def __str__(self):
        return self.titulo

class quarto(models.Model):
    tipo_quarto = [
        ("Solteiro", "Solteiro"),
        ("Premium", "Premium"),
        ("Plus", "Plus")
    ]
    status_status = [
        (1, "Disponível"),
        (0, "Reservado")
    ]

    num_quarto = models.IntegerField()
    qnt_hospedes = models.IntegerField()
    tipo = models.CharField(choices=tipo_quarto, max_length=20)
    valor = models.FloatField(max_length=3)
    descricao = models.TextField()
    status = models.BooleanField(choices=status_status, default=1)
    img = models.ImageField(upload_to='quartos/')

    def __str__(self):
        return f'{self.tipo} - {self.num_quarto}'

class Reserva(models.Model):
    quarto = models.ForeignKey(quarto, on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=100)
    telefone_cliente = models.CharField(max_length=20)
    data_checkin = models.DateField()
    data_checkout = models.DateField()

    def __str__(self):
        return f"{self.nome_cliente} - Quarto {self.quarto.num_quarto} de {self.data_checkin} até {self.data_checkout}"

