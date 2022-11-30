from django.contrib import admin

from .models import Paciente, Funcionario, Medico, Servico, Documento


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'endereco', 'perfil', 'convenio')
    
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'endereco', 'perfil', 'matricula')

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'endereco', 'perfil', 'matricula', 'crm')
    
@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
    
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'documentos')

    

    