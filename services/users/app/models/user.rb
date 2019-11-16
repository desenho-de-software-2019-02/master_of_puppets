class User < ApplicationRecord
  devise :database_authenticatable,
          :registerable,
          :rememberable,
          :timeoutable,
          :jwt_authenticatable,
          jwt_revocation_strategy: JwtBlacklist
end
