Feature: Cart flow

    Scenario: Validate the cart flow
        Given I access the Giuliana Flores website
        When I click in the login button
        And I inform the email emanuel-campos88@acaoi.com.br and the password CFIMA5qmR6
        When I choose the banner and the product
        And I inform zip code and date of delivery
        And I include the product in the cart 
        Then I check the name and price
        