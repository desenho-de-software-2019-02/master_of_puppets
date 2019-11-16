class ApplicationController < ActionController::API
  respond_to :json

  private

  def respond_with(resource, _opts = {})
    render json: resource
  end

  def respond_to_on_destroy
    head :no_content
  end
  
  # def render_resource(resource)
  #   if resource.errors.empty?
  #     render json: resource
  #   else
  #     validation_error(resource)
  #   end
  # end

  # def validation_error(resource)
  #   render json: {
  #     errors: [
  #       {
  #         status: '400',
  #         title: 'Bad Request',
  #         detail: resource.errors,
  #         code: '100'
  #       }
  #     ]
  #   }, status: :bad_request
  # end
end
