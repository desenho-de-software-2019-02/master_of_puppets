from models.classes_models import create_new_class, verify_if_class_exists, read_classes, remove_class

def validate_new_class_to_model(data):

    # Validar os dados da classe
    if verify_if_class_exists(data):
        return "class already exists"

    return create_new_class(data)


def get_class():
    return read_classes()

def delete_class(data):
    if verify_if_class_exists(data):
        return remove_class(data)
    return 'class doesnt exist'

