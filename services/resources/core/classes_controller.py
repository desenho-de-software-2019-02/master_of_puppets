from models.classes_models import create_new_class, verify_if_class_exists, read_classes, att_class, remove_class, info

def validate_new_class_to_model(data):

    # Validar os dados da classe
    if verify_if_class_exists(data['name']):
        return "class already exists"

    return create_new_class(data)


def get_class():
    return read_classes()

def update_class(data):
    if verify_if_class_exists(data['old_name']):
        return att_class(data)
    return 'class doesnt exist'

def delete_class(data):
    if verify_if_class_exists(data['name']):
        return remove_class(data)
    return 'class doesnt exist'

def class_info(data):
    if verify_if_class_exists(data['name']):
        return info(data)
    return 'class doesnt exist'

