class AuthController < ApplicationController
    protect_from_forgery with: :null_session

    def register
        @user = User.new(params[:user])
        if @user.save
            render :json => @user
        else
            render :json => { error: "Bad user input" }
        end
    end

    def login

    end
end
