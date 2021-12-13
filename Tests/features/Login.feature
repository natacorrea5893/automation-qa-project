@regression @Login
Feature: Login in Store
  As a user
  I want to access the Store Page
  So Login correctly

  Background:
    Given the Store webPage

  Scenario: Login in Store Page correctly
    When complete "agusDarwoft" and "automation"
    Then Login correctly

  Scenario Outline: Complete user and password wrong
    When complete "<User>" and "<Password>"
    Then I get an Incorrect Login message "Error: Incorrect login or password provided."

    Examples: User and Password combinations
      | User       | Password   |
      |agusDarwoft | 123        |
      | .          | 123        |
      | a          | automation |