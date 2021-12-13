Feature: Login in Store
  As a user
  I want to access the Store Page
  So Login correctly

  Scenario: Login in Store Page correctly
  Given the Store webPage
  When complete "agusDarwoft" and "automation"
  Then Login correctly

  Scenario: Complete user and password wrong
  Given the Store webPage
  When complete "agusDarwoft" and " "
  Then I get an Incorrect Login message "Error: Incorrect login or password provided."