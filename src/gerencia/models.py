from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    perfil = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Paciente(Usuario):
    convenio = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class Funcionario(Usuario):
    matricula = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"


class Medico(Funcionario):
    crm = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

class Documento(models.Model):
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"


class Servico(models.Model):
    tipo = models.CharField(max_length=30)
    documentos = models.ForeignKey(Documento, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"


