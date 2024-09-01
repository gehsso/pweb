from django import forms
from .models import Produto
from django.core.exceptions import ValidationError



class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome',  'preco']

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco is not None and preco < 10:
            raise ValidationError("O preço deve ser igual ou maior que 10.<br>")
        return preco













    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:  # Verifica se o nome está vazio ou é uma string vazia
            raise forms.ValidationError("O campo nome não pode ser vazio.<br>")
        if len(nome) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.<br>")
        return nome