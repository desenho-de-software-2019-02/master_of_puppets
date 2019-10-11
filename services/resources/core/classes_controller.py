from models.classes_models import modelsClasses

class controllerClasses():
    def validate_new_class_to_model(data):
        return modelsClasses.create_new_class(data)

    def get_class():
        return modelsClasses.read_classes()

    def update_class(data):
        if modelsClasses.verify_if_class_exists(data['_id']):
            return modelsClasses.att_class(data)
        return 'class doesnt exist'

    def delete_class(data):
        if modelsClasses.verify_if_class_exists(data['_id']):
            return modelsClasses.remove_class(data)
        return 'class doesnt exist'

    def class_info(data):
        if modelsClasses.verify_if_class_exists(data["_id"]):
            return modelsClasses.info(data)
        return 'class doesnt exist'

