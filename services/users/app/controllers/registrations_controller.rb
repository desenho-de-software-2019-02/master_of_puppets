# class RegistrationsController < Devise::RegistrationsController
#   respond_to :json
  
#   def create
#     build_resource(sign_up_params)
#     resource.save()
#     render_resource(resource)
#   end
# end
class RegistrationsController < Devise::SessionsController
  before_action :authenticate_user!, except: [:create]
  respond_to :json
end
