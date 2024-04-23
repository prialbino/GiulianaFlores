Feature: Sign up an account

    Scenario: Sign up a new account
        Given I access the Giuliana Flores website
        When I click in the login button
        When I inform all the mandatory information for the new sign up
        Then I will be successfully directed to a Home page

    Scenario: Successfully Sign in  
        Given I access the Giuliana Flores website
        When I click in the login button
        And I inform the email kaique-dacunha92@otlokk.com and the password ctnj41Efxi
        Then I will be successfully directed to a Home page 

    Scenario: Invalid Sign in 
        Given I access the Giuliana Flores website
        When I click in the login button
        And I inform the email kaique-dacunha92@otlokk.com and the password water10
        Then shows the login ATENÇÃO - e-mail ou senha inválidos! error 
    


