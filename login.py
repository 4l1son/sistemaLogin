from model import login_model

cadastros = [
    {
        'id': 1,
        'name': 'alisson',
        'senha': 'alisson'
    }

]
def validate(model:login_model):

   for cadastro in cadastros:
       return cadastro