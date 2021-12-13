Feature: Manage Address Book Entries
  As a user
  I want to manage the Book Entries
  So Edit Address correctly

  Background:
    Given the Store webPage

  Scenario: Add an address entry correctly
    When complete "agusDarwoft" and "automation"
    And click on "Manage Address Book"
    And click on "New Address"
    And complete "Natanael", "Correa", "Calle Falsa 123", "Jesús María", "Cordoba", "5220", "Argentina"
    And click Continue button
    Then new address is saved correctly
