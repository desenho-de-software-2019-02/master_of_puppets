from models.classes_models import create_new_class, verify_if_class_exists

def validate_new_class_to_model(data):

    # Validar os dados da classe
    if verify_if_class_exists(data['name']):
        return "class already exists"

    create_new_class(data)

    return "'{}' sucessfully added".format(data['name'])

