require 'test_helper'

class AuthTest < ActionDispatch::IntegrationTest
  # test "the truth" do
  #   assert true
  # end
  test "register" do
    post "/register", user[username]
  test "login" do
    post "/login", username: users(:k26dr).username, password: users(:k26dr).password
    assert_response :success
end
