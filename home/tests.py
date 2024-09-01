import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pweb.settings')
django.setup()

from home.models import Produto


produto = Produto(nome='Teste', preco=10.99)
produto.save()
print('Produto inserido com sucesso!')



ef form_produto(request):
    form = ProdutoForm()
    if request.method == 'POST':
        ## Faça isso
    else:
        ## faça


if request.method == 'POST':
## Faça isso
else:
## faça aquilo

