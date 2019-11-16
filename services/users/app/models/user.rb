class User
  include Mongoid::Document
  field :username, type: String
  field :email, type: String
  field :password, type: Digest

  devise :database_authenticatable,
          :jwt_authenticatable,
          jwt_revocation_strategy: JWTBlacklist
end
