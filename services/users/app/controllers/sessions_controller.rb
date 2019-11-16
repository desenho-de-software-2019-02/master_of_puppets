# class SessionsController < Devise::SessionsController
#   respond_to :json

#   private

#   def respond_with(resource, _opts = {})
#     render json: resource
#   end

#   def respond_to_on_destroy
#     head :no_content
#   end
# end
class SessionsController < Devise::SessionsController
  before_action :authenticate_user!, except: [:create, :new]
  respond_to :json
private
  def respond_with(resource, _opts = {})
      render json: resource
    end
  def respond_to_on_destroy
    head :ok
  end
end
