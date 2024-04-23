Feature: Cart flow

    Scenario: Validate the cart flow
        Given I access the Giuliana Flores website
        When I click in the login button
        And I inform the email kaique-dacunha92@otlokk.com and the password ctnj41Efxi
        When I choose the banner and the product
        And I inform zip code and date of delivery
        And I include the product in the cart 
        Then I check the name and price
        