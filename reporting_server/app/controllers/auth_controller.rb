class AuthController < ApplicationController
    protect_from_forgery with: :null_session

    def register
        user = User.new(user_params)
        if user.save
            user.password_digest = nil
            render :json => { id: user.id, username: user.username }
        else
            render :json => { error: "Bad user input" }
        end
    end

    def login
        user = User.find_by(username: params[:username])
        if user && user.authenticate(params[:password])
            render :json => { success: true }
            # create jwt
        else
            render :json => { error: "Bad credentials" }
        end
    end

    private

      def user_params
        params.require(:user).permit(:username, :password)
      end
end
