require "net/http"
require "uri"

@tests = 0
@tests_failed = 0
@tests_passed = 0 
@name = false
@assignment = false
@server_url = "http://localhost:5000/attempt"

def assert statement
    # get line number of test
    stack = caller.to_s
    first_index = stack.index(':') + 1
    length = stack.index(':', first_index) - first_index
    line = stack[first_index, length]

    @tests += 1
    if statement
        @tests_passed += 1
        puts "Test #{@tests} on line #{line} \033[32mPass\033[0m"
    else
        @tests_failed += 1
        puts "Test #{@tests} on line #{line} \033[31mFail\033[0m"
    end
end

def report
    puts "Sending report to server"
    if not @assignment
        puts "Report not sent. @assignment must be set"
    elsif not @name
        puts "Report not sent. @name must be set"
    else
        uri = URI.parse(@server_url)
        Net::HTTP.post_form(uri, {
            "student" => @name,
            "assignment" => @assignment,
            "tests_passed" => @tests_passed,
            "tests_failed" => @tests_failed
        })
        puts "Report sent"
    end
end
    
