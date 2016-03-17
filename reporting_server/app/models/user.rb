class User < ActiveRecord::Base
    validates :username, :presence => true, :uniqueness => true, :length => { :in => 3..20 }
    validates :password, presence: true, length: { minimum: 6 }
    has_secure_password
end

